#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[]) {
    //Loading matrix
    ifstream input(argv[1]);
    int size;
    input >> size; 
    int matrix[size][size];      
    for(int i = 0; i < size; ++i) {
        for(int j = 0; j < size; ++j) {
            input >> matrix[i][j];
        }   
    }
    input.close();

    //////// Algorithm    
    for(int i = 0; i < size; ++i) {
        for(int j = 0; j < size; ++j) {
            if (i != j) {
                matrix[i][j] = 1 - matrix[i][j];
            } else {
                matrix[i][j] = 0;
            }
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }    
    //Saving new matrix
    fstream output;
    output.open(argv[1]);
    output.clear();
    output << size << "\n";    
    for(int i = 0; i < size; ++i) {
        for(int j = 0; j < size; ++j) { 
            output << matrix[i][j];
            if (j != size - 1) {
                output << " ";
            }
        }
        if (i != size - 1) {
            output << "\n";
        }
    }
    output.close();
}
