#include "stdlib.h"
#include "stdio.h"
#include <iostream>




using namespace std;


typedef struct element_s {
    struct element_s *next, *prev;
    bool used;
    size_t size;
} element_t;

#define FOREACH(I, HEAD) for(I=HEAD;I!=NULL;I=I->next)

#define INSERT(NEW, ELEM)           \
{                                   \
    if (ELEM->next != NULL) {       \
        ELEM->next->prev = NEW;     \
    }                               \
    NEW->next = ELEM->next;         \
    ELEM->next = NEW;               \
    NEW->prev = ELEM;               \
}           

element_t *head = NULL;

void init(size_t size) {
    if (size <= sizeof(element_t)) {
        cout << "ERROR: Too small size." << endl;
    }
    head = (element_t *)malloc(size);
    head->used = false;
    head->size = size - sizeof(element_t);
    head->next = NULL;
    head->prev = NULL;
    //return head;
}

void *alloc(size_t size) {
    element_t *elem = NULL, *nelem = NULL;
    void *res = NULL;
    FOREACH(elem, head) {
        if (!elem->used and elem->size >= size) {
            res = elem + sizeof(element_t);
            nelem = (element_t *)(res + size);
            nelem->used = false;
            nelem->size = elem->size - size - sizeof(element_t);
            INSERT(nelem, elem);
            elem->used = true;
            elem->size = size;
            return res;
        }    
    }
}

void print_list() { 
    element_t *elem = NULL;
    FOREACH(elem, head) {
        printf("pointer %p used %u size %u\n", elem, elem->used, elem->size);
    }
    
}

void mfree(void *link) {
    element_t *elem = NULL, *nelem = NULL;
    FOREACH(elem, head) {
        if (elem + sizeof(element_t) == link) {

        }
    }

}

int main() {
    init(1000);
    for (int i = 0; i < 10; ++i) {
        void *t = alloc(10);
    }
    //printf("head %p, t %p\n", head, t);
    //printf("size of element %u\n", sizeof(element_t));
    print_list();
}
