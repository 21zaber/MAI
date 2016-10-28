#include "stdlib.h"
#include "stdint.h"
#include "stdio.h"
#include <iostream>




using namespace std;


typedef struct element_s {
    struct element_s *next, *prev;
    bool used;
    size_t size;
} element_t;

#define FOREACH(I, HEAD) for(I=HEAD;I!=NULL;I=I->next)
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

#define MERGE_NEXT(ELEM)                                               \
{                                                                      \
    if (ELEM->next!=NULL and !(ELEM->used) and !(ELEM->next->used)) {  \
        ELEM->size += ELEM->next->size + sizeof(element_t);            \
        DELETE(ELEM->next);                                            \
    }                                                                  \
}
                       
#define SUM(L, K, TYPE) (TYPE)((uint64_t)L + (uint64_t)K)
#define SUB(L, K, TYPE) (TYPE)((uint64_t)L - (uint64_t)K)


element_t *head = NULL;



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
}

void *alloc(size_t size) {
    element_t *elem = NULL, *nelem = NULL;
    element_t *res = NULL;
    FOREACH(elem, head) {
        if (!elem->used and elem->size >= size) {
            res = SUM(elem, sizeof(element_t), element_t*);
            nelem = SUM(res, size, element_t*); 
            nelem->used = false;
            nelem->size = elem->size - size - sizeof(element_t);
            INSERT(nelem, elem);
            elem->used = true;
            elem->size = size;
            cout << "Allocation: " << size << " bytes" << endl;
            return res;
        }    
    }
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
    cout << "Deallocation: " << elem->size << " bytes" << endl;
    MERGE_NEXT(elem);
    MERGE_NEXT(elem->prev);
}

void print_list() { 
    element_t *elem = NULL;
    cout << "List of blocks:" << endl;
    int i = 0;
    FOREACH(elem, head) {
        printf("  %d: used %u, size of block %lu bytes\n", i, elem->used, elem->size);
        i++;
    }
    printf("\n");
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


int main() {
    test1();
    //printf("head %p, t %p\n", head, t);
    //printf("size of element %u\n", sizeof(element_t));
}
