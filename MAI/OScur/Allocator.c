#include "Allocator.h"

void *Allocator(uint64_t Size) {
    TItem * cur;
    TItem * nec;
    cur = nec = Head;
    int flag = 0;
    uint64_t maxTmp = max(sizeof(TItem), Size);
    if (cur->sizeBlock >= maxTmp) {
        nec = cur;
        flag = 1;
    }
    while(cur) {
        printf("cur in while %llu\n", cur);
        if (cur->sizeBlock >= nec->sizeBlock && cur->sizeBlock >= maxTmp) {
            nec = cur;
            flag = 1;
        }
        cur = cur->next;
    }
    if (flag == 0) {
        printf("Error, out of memory\n");
        exit(2);
    }

    cur = nec;
    uint64_t tmpSize = cur->sizeBlock;
    TItem * nextTmp = cur->next;
    TItem * prevTmp = cur->prev;

    if ((maxTmp  == sizeof(TItem) && cur->sizeBlock - maxTmp <= 0) || (maxTmp == Size && cur->sizeBlock - maxTmp <= 0)) {
        if (cur->next) {
            cur->next->prev = cur->prev;
        }
        if (cur->prev) {
            cur->prev->next = cur->next;
        }
        cur->prev = cur->next = NULL;
    }
    cur = (char*)cur + maxTmp;
    cur->next = nextTmp;
    cur->prev = prevTmp;
    cur->sizeBlock = tmpSize - maxTmp;

    if (cur >= Head) {
        Head = cur;
    }
    return nec;
}

void Free(void *del, uint64_t size) {
    TItem * cur = Head;
    TItem * prev = NULL;

    uint64_t maxTmp = max(size, 24);

    while (cur && cur < del) {
        prev = cur;
        cur = cur->next;
    }
    
    TItem * tmp = (char*)del;
    if (prev)
        prev->next = tmp;
    tmp->next = cur;
    tmp->prev = prev;
    if (cur)
        cur->prev = tmp;
    tmp->sizeBlock = maxTmp;
    if (tmp->prev && ((char*)tmp->prev + tmp->prev->sizeBlock == (char*)tmp)) {
        tmp->prev->next = tmp->next;
        tmp->prev->sizeBlock += tmp->sizeBlock;
        if (tmp->next)
            tmp->next->prev = tmp->prev;
        tmp = tmp->prev;
    }
    if (tmp->next && (char*)tmp->next - maxTmp == (char*)tmp) {
        tmp->sizeBlock += tmp->next->sizeBlock;
        tmp->next = tmp->next->next;
        if (tmp->next)
            tmp->next->prev = tmp;
    }
    if (Head >= tmp)
        Head = tmp;
}

uint64_t max(const uint64_t a, const uint64_t b) {
    return a >= b : a ? b;
}
