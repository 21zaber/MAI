#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct item_s {
    struct item_s *next, *prev;
    uint64_t sizeBlock;
} item_t;

item_t * head;
static unsigned long long const int memsize = 1 << 20;
void *memory;

void *allocator(uint64_t);
void myfree(void * , uint64_t);
uint64_t max(const uint64_t, const uint64_t);
