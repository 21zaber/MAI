#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define NAME_LEN 35
#define SIZE 32000
#define NAME_TYPE char[NAME_LEN]

typedef struct {
    int value;           // item value
    int used;            // flag of usage
    int prev_free;       // link to prev free elem
    int next_free;       // link to next free elem
    char name[NAME_LEN]; // name of element
} mem_element;

// structure initialization
mem_element* memory = NULL;

void my_malloc(int size, char name[NAME_LEN]) {
	int n = 0, m = 0, p = -1, check = -1;
	if (size > 1) {
 	    while (m < SIZE) {
            for(int k = m; k < m + size - 1; k++) {
                if(memory[k].used != 0) {
                    p = k;
                }
            }
            if (n == 0 && p == -1) {
                check = m;
                n++;
            } else if (p == -1 && n == 1 && m + size <= SIZE) {
                for(int j = m;j < m + size;j++) {
                    memory[j].used = 1;
                    memory[j].prev_free = m;
                    memory[j].next_free = m + size;
                    strcpy(memory[j].name, name);
                }
                // Success
                return;
            } else if (p != -1) {
                m = memory[p].next_free;
                p = -1;
            }
            m++;
            if(m + size >= SIZE) {
                break;
            }
        }
    } else if(size == 1) {
        while (m < SIZE) {
            if(memory[m].used != 0) {
                p = m;
            }
            if (n == 0 && p == -1) {
                check = m;
                n++;
            } else if (p == -1 && n == 1 && m + size <= SIZE) {
                memory[m].used = 1;
                memory[m].prev_free = m;
                memory[m].next_free = m + size;
                strcpy(memory[m].name, name);
                // Success
                return;
            } else if (p != -1) {
                m = memory[p].next_free - 1;
                p = -1;
            }
            m++;
            if(m >= SIZE) {
                break;
            }
        }
    }
	if (check != -1 && check + size <= SIZE) {
		m = check;
		for(int j = m;j < m + size;j++) {
			memory[j].used = 1;
			memory[j].prev_free = m;
			memory[j].next_free = m + size;
			strcpy(memory[j].name, name);
		}
        // Success
		return;
	}
    // No memory 
	return;
}

void my_free(char name[NAME_LEN]) {
	int m = 0;
	while (m < SIZE) {
		if(memory[m].used != 0) {
			if(strcmp(memory[m].name, name) == 0) {
				for(int k = memory[m].prev_free; k < memory[m].next_free; k++) {
					memory[k].used = 0;
					memory[k].prev_free = 0;
					memset(memory[k].name, 0, sizeof(memory[k].name));
				}
				return;
			} else {
                m = memory[m].next_free;
            }
		}
		m++;
	}
	return;
}

int main(int argc, char **argv) {
    memory = (mem_element*) calloc(SIZE, sizeof(mem_element));

	for(int i = 0; i < 1000; i++) {
		my_malloc(32, "test_name");
	}

	free(memory);
	return 0;
}
