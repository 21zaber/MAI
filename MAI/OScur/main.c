#include "dlist.h"

int main() {
    memory = (void*)malloc(memsize);
    if (memory == NULL) {
        printf("Error, little memory\n");
        exit(1);
    }
    printf("Malloc %llu bytes\n", memsize);

    head = memory;
    head->next = Head->prev = NULL;
    head->sizeBlock = memsize - sizeof(item_t);
    int c;
    int sizeString = 0;

    TList * list = Allocator(sizeof(TList));
    int i = 1;
    Create(list);
    while ((c = getchar()) != EOF) {
        switch(c) {
            case '+':
                if (Push(list) == true) {
                    printf("OK!\n");
                }
                else {
                    printf("Error!\n");
                }
                break;
            case 's':
                PrintSize(list);
                break;
            case 'p':
                PrintList(list);
                break;
            case '-':
                if (Delete(list) == true) {
                    printf("OK!\n");
                }
                else {
                    printf("Error!\n");
                }
                break;
                
            case 'q':
                return 0;
        }
    }
    return 0;
}
