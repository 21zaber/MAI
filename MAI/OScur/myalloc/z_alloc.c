#include "z_alloc.h"
#include "dlist.h"
#include "stdlib.h"
#include "stdbool.h"

typedef struct memblock_s {
    void *memory;
    uint64_t size;
    bool used;
    struct memblock_s *next, *prev;    
} memblock_t;

typedef struct allocator_s {
    uint64_t total_size;    
    uint64_t free_memory_size;    
    uint64_t used_memory_size;    

    memblock_t *head;
} allocator_t;

allocator_t allocator;

void z_destroy() {
    if (allocator.total_size == 0) {
        return;
    }
    free((void *)allocator.head);
    allocator.total_size = allocator.free_memory_size = allocator.used_memory_size = allocator.head = 0;
}

void z_init(uint64_t size) {
    allocator.total_size = size;
    allocator.free_memory_size = size - sizeof(memblock_t);
    allocator.used_memory_size = sizeof(memblock_t);
    void *mem = malloc(size);
    memblock_t *head = mem;
    head->memory = mem + sizeof(memblock_t);
    head->size = allocator.free_memory_size;
    head->used = false;
    DL_APPEND(allocator.head, head);
}

void try_unite(memblock_t *block) {
    if (!block || block->used) {
        return;
    }
    memblock_t *prev = block->prev;
    memblock_t *next = block->next;
    if (!prev || prev == block || prev->used) {
        return;
    }
    prev->size += block->size + sizeof(memblock);
    DL_DELETE(allocator.head, block);
    try_unite(prev);
    try_unite(next);
}

void z_free(void *link) {
    if (allocator.total_size == 0) {
        return;
    }
    memblock_t *block, *tmp;
    DL_FOREACH_SAFE(allocator, block, tmp) {
        if (block.memory == link && block.used) {
            block.used = false;
            try_unite(block);
            break;
        }
    }
}

void *z_alloc(uint64_t size) {
    return NULL;
}
