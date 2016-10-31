#include "stdlib.h"
#include "stdint.h"
#include "stdio.h"
#include "string.h"  
#include <ctime>
#include <iostream>
#include <vector>

#define SIMPLE 1

//#define LOGS 1

using namespace std;

typedef struct element_s {
    struct element_s *next, *prev;
    bool used;
    size_t size;
} element_t;

#define FOREACH(I, HEAD) for(I=HEAD;I!=NULL&&I->next!=I;I=I->next)
#define FOREACH_SAFE(I, HEAD, TMP) for(I=HEAD,TMP=I->next;(I!=NULL)and(TMP=I->next);I=TMP)


#define INSERT(NEW, ELEM)           \
{                                   \
    if (ELEM->next != NULL) {       \
        ELEM->next->prev = NEW;     \
    }                               \
    NEW->next = ELEM->next;         \
    ELEM->next = NEW;               \
    NEW->prev = ELEM;               \
}         

#define DELETE(ELEM)                      \
{                                         \
    if (ELEM->next != NULL) {             \
        ELEM->next->prev = ELEM->prev;    \
    }                                     \
    if (ELEM->prev != NULL) {             \
        ELEM->prev->next = ELEM->next;    \
    }                                     \
}

#define MERGE_NEXT(ELEM)                                                   \
{                                                                          \
    if (ELEM!=NULL){                                                       \
        if (ELEM->next!=NULL and !(ELEM->used) and !(ELEM->next->used)) {  \
            ELEM->size += ELEM->next->size + sizeof(element_t);            \
            DELETE(ELEM->next);                                            \
        }                                                                  \
    }                                                                      \
}
                       
#define SUM(L, K, TYPE) (TYPE)((uint64_t)L + (uint64_t)K)
#define SUB(L, K, TYPE) (TYPE)((uint64_t)L - (uint64_t)K)


element_t *head = NULL;
size_t allocated = 0;



void init(size_t size) {
    if (size <= sizeof(element_t)) {
        cout << "ERROR: Too small size." << endl;
    }
    head = (element_t *)calloc(size, 1);
    head->used = false;
    head->size = size - sizeof(element_t);
    head->next = NULL;
    head->prev = NULL;
    cout << "Initialization: " << size << " bytes" << endl;
    allocated = size;
}

void *alloc(size_t size) {
    element_t *elem = NULL, *nelem = NULL;
    element_t *res = NULL;
#ifdef SIMPLE
    FOREACH(elem, head) {
        if (!elem->used and elem->size >= size) {
            size_t excess_mem = elem->size - size - sizeof(element_t); 
#ifdef LOGS
            cout << "Allocation:   " << size << " bytes" << endl;
#endif
            if (elem->size > size + sizeof(element_t)) {
                res = SUM(elem, sizeof(element_t), element_t*);
                nelem = SUM(res, size, element_t*); 
                nelem->used = false;
                nelem->size = excess_mem;
                INSERT(nelem, elem);
                elem->used = true;
                elem->size = size;
                return res;
            } else {
                res = SUM(elem, sizeof(element_t), element_t*);
                elem->used = true;
                return res;
            }
        }    
    }
#else 
    element_t *best = NULL;
    FOREACH(elem, head) {
        if (!elem->used and elem->size >= size) {
            if (best == NULL or best->size > elem->size){
                best = elem;
                //cout << "1";
            }    
        }    
    }

    if (best != NULL) {
        size_t excess_mem = best->size - size - sizeof(element_t); 
#ifdef LOGS
        cout << "Allocation:   " << size << " bytes" << endl;
#endif
        if (best->size > size + sizeof(element_t)) {
            res = SUM(best, sizeof(element_t), element_t*);
            nelem = SUM(res, size, element_t*); 
            nelem->used = false;
            nelem->size = excess_mem;
            INSERT(nelem, best);
            best->used = true;
            best->size = size;
            return res;
        } else {
            res = SUM(best, sizeof(element_t), element_t*);
            best->used = true;
            return res;
        }
    }
#endif

#ifdef LOGS
    cout << "Allocation:   " << size << " bytes. FAIL" << endl;
#endif
    return NULL;
}

void try_to_merge() {
    element_t *elem, *i;
    FOREACH_SAFE(elem, head, i) {
        if (elem->next != NULL and !(elem->used) and !(elem->next->used)) {
            elem->size += elem->next->size + sizeof(element_t);
            DELETE(elem->next);
        }
    }
}

void dealloc(void *l) {
    element_t *elem = SUB(l, sizeof(element_t), element_t*);
    elem->used = false;
#ifdef LOGS
    cout << "Deallocation: " << elem->size << " bytes" << endl;
#endif
    MERGE_NEXT(elem);
    MERGE_NEXT(elem->prev);
}

void print_list() { 
    element_t *elem = NULL;
    cout << "List of blocks:" << endl;
    int i = 0;
    FOREACH(elem, head) {
        printf("  %d: used %u, size of block %lu bytes", i, elem->used, elem->size);
        // DEBUG print pointers
        //printf(" link %p next %p prev %p\n", elem, elem->next, elem->prev);
        cout << endl;
        i++;
    }
}

#define BUF_SIZE 150

void print_mem_usage() {
    char buf[BUF_SIZE+1];
    memset(buf, '.', BUF_SIZE);
    buf[BUF_SIZE] = '\0';
        
    element_t *elem = NULL;
    size_t prev = 0;
    size_t used_mem = 0;
    size_t sys_mem = 0;
    size_t _mem = 0;

    FOREACH(elem, head) {
        int p = prev * BUF_SIZE / allocated;
        if (elem->used) {
            _mem += elem->size + sizeof(element_t);
            used_mem += elem->size;
        } else {
            int n = _mem * BUF_SIZE / allocated;
            memset(buf+p, '|', n);
            prev += _mem + sizeof(element_t) + elem->size;
            _mem = 0;
        }
        used_mem += sizeof(element_t);
        sys_mem += sizeof(element_t);
    }
    float per_u = (float)(used_mem * 100) / allocated;
    float per_s = (float)(sys_mem * 100) / allocated;

    cout << "Memory usage: " << endl;
    cout << '\t' << '[' << buf << ']' << endl;
    printf("\t%.2f", per_u);
    cout << "\% of memory used." << endl;
    printf("\t%.2f", per_s);
    cout << "\% of memory used by allocator." << endl;
}

void destroy() {
    element_t *elem = NULL;
    FOREACH(elem, head) {
        elem->used = false;
    }
    cout << "Destroying" << endl;
    free((void *)head);
}

void test1() {
    init(1000);
    void* t[10];
    for (int i = 0; i < 10; ++i) {
        t[i] = alloc(10);
    }
    print_list();
    dealloc(t[3]);
    print_list();
    dealloc(t[5]);
    print_list();
    dealloc(t[4]);
    print_list();
    destroy();
}

void test2(size_t total_mem, uint32_t n, size_t max_block, size_t min_block) {
    init(total_mem);
    vector<void*> elements;
    for (int i = 0; i < n; ++i) {
        if ((rand() % 2) == 0 and elements.size() > 0) {
            int n = rand() % elements.size();
            dealloc(elements[n]);
            elements.erase(elements.begin() + n);
        } else {
            size_t sz = rand() % (max_block - min_block + 1) + min_block;
            void *new_elem = alloc(sz);
            if (new_elem != NULL) {
                elements.push_back(new_elem);
                memset(new_elem, 0, sz);
            }
        }
        if (i % (int)(n / 10) == 0){
            //print_list();
            //printf("\n");
            print_mem_usage();
            printf("\n");
        }
    }
    destroy();
}


int main() {
    srand (time(NULL));
    //test2(10*1000, 1000, 500, 500);
    test2(10*1000, 1000, 1000, 100);
}
