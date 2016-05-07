#include "dlist.h"

void Create(TList * list) {
    list->Size = 0;
    list->Head = NULL;
    NIL = Allocator(sizeof(TLI));
    NIL->prev = NULL;
    NIL->next = NULL;
    NIL->string = NULL;
    list->Head = NIL;
}

bool Push(TList * list)
{
//    printf("______FUNC ADD___________\n");
    int n;
    int sizeString;
    printf("Place: ");
    scanf("%d", &n);
//    printf("n -- %d  size -- %d\n", n, list->Size);
    if(n < 0 || n > list->Size + 1) {
        return false;
    }
    printf("The number of letters: ");
    scanf("%d", &sizeString);
    TLI * p = Allocator(sizeof(TLI));
    p->string = Allocator(sizeof(TData) * (sizeString + 1));
    int c;
    int i = 0;
    getchar();
    while((c = getchar()) != EOF) {
        if (i == sizeString) {
            p->string[i] = '\0';
            break;
        }
        if (c == '\n') {
        }
        else {
            p->string[i++] = c;
        }
    }
//    printf("__ADD: %s___\n", p->string);
    if (list->Head == NIL) {
        list->Head = p;
        NIL->prev = p;
        p->next = NIL;
        NIL->next = p;
        p->prev = NIL;
    }
    else {
        list->Iter = list->Head;
        for (i = 0; i < n - 1; i++) {
            list->Iter = list->Iter->next;
        }
        p->prev = list->Iter->prev;
        if (list->Iter->prev)
            list->Iter->prev->next = p;
        p->next = list->Iter;
        list->Iter->prev = p;
        if (n == 1)
            list->Head = p;
    }
    list->Size++;
    return true;
}

void PrintSize(TList * list)
{
    printf("Size list: %d\n", list->Size);
}

void PrintList(TList * list)
{
    if(list->Size == 0) {
        printf("Empty!\n");
        return;
    }
    int i;
    list->Iter = list->Head;
    for (i = 0; i < list->Size; i++) {
        printf("%s", list->Iter->string);
        if (list->Iter->next != NIL) {
            printf(" -> ");
        }
        list->Iter = list->Iter->next;
    }
    printf("\n");
}

bool Delete(TList * list)
{
//    printf("______FUNC DELETE___________\n");
    int n;
    printf("Remove an item under the number: ");
    scanf("%d", &n);
    if (n < 0 || list->Size < n)
        return false;
    list->Iter = list->Head;
    int i;
    for (i = 0; i < n - 1; i++) {
        list->Iter = list->Iter->next;
    }
    if (list->Iter->prev != NIL) {
        list->Iter->prev->next = list->Iter->next;
    }
    else {
        list->Head = list->Iter->next;
    }
//    if(list->Iter->next != NIL) {
    list->Iter->next->prev = list->Iter->prev;
//    }
    Free(list->Iter->string, sizeof(TData) * strlen(list->Iter->string));
    Free(list->Iter, sizeof(TLI));
    list->Size--;
    return true;
}
