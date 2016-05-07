#pragma once

#include "Allocator.h"
#include <string.h>
#include <stdbool.h>

typedef char TData;

typedef struct list_item_s {
    struct list_item_s *next, *prev;
    TData *string;
} list_item_t;

typedef struct dlist_s {
    list_item_t *head;
    list_item_t *iter;
    int size;
} dlist_t;

list_item_t *NIL;

void Create(TList*);
bool Push(TList*);
void PrintSize(TList*);
void PrintList(TList*);
