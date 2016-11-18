#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>
#include <map>

using namespace std;

int main(int argc, char *argv[]) {
    //Loading matrix
    ifstream input(argv[1]);
    int sizex, sizey;
    input >> sizex >> sizey; 
    int matrix[sizex][sizey];      
    for(int i = 0; i < sizex; ++i) {
        for(int j = 0; j < sizey; ++j) {
            input >> matrix[i][j];
        }   
    }
    input.close();
    set<int> used_row;
    set<int> used_col;
    int marked_row[sizex];
    //int marked_col[size];

    for (int i = 0; i < sizex; ++i) {
        marked_row[i] = -1;
        //marked_col[i] = -1;
    }

    bool flag = false;
    while (1) {
        if (used_row.size() >= sizex or flag or
            used_col.size() >= sizey) {
            break;
        }
        flag = true;
        for (int i = 0; i < sizey; ++i) { // search for unused column
            if (used_col.find(i) != used_col.end()) {
                continue;
            }
            //printf("i: %d\n", i);
            for (int j = 0; j < sizex; ++j) { // search for edge in this column that not in answer, but row is used
                if (flag and matrix[j][i] == 1 and marked_row[j] != -1) {
                    //printf("j1: %d\n", j);
                    for (int t = 0; t < sizex; ++t) { // search for unused row in column marked_row[j]
                        if (flag and matrix[t][marked_row[j]] == 1 and used_row.find(t) == used_row.end()) {
                            //printf("\t c1 %d r1 %d c2 %d r2 %d\n", i, j, marked_row[j], t);
                            matrix[j][i] = 2;
                            matrix[j][marked_row[j]] = 1;
                            matrix[t][marked_row[j]] = 2;
                            used_col.insert(i);    
                            used_row.insert(t);    
                            marked_row[t] = marked_row[j];
                            marked_row[j] = i;
                            flag = false;
                        }
                    }
                } else if (flag and matrix[j][i] == 1 and marked_row[j] == -1) {
                    //printf("j2: %d\n", j);
                    //printf("\t i %d j %d\n", i, j);
                    marked_row[j] = i;
                    matrix[j][i] = 2;
                    used_col.insert(i);    
                    used_row.insert(j);  
                    flag = false;  
                }
            }
        }
        for (int i = 0; i < sizex; ++i) {
            for (int j = 0; j < sizey; ++j) {
                //printf("%d ", matrix[i][j]);
                //matrix[i][j] = max(0, matrix[i][j] - 1);
            }
           // printf("\n");
        }
        //printf("\n");
       // printf("\n");
    }

    for (int i = 0; i < sizex; ++i) {
        for (int j = 0; j < sizey; ++j) {
            //printf("%d ", matrix[i][j]);
            matrix[i][j] = max(0, matrix[i][j] - 1);
        }
        //printf("\n");
    }



    //Saving new matrix
    fstream output;
    output.open(argv[1]);
    output.clear();
    output << sizex << "\n" << sizey << "\n";    
    for(int i = 0; i < sizex; ++i) {
        for(int j = 0; j < sizey; ++j) { 
            output << matrix[i][j];
            if (j != sizey - 1) {
                output << " ";
            }
        }
        if (i != sizex - 1) {
            output << "\n";
        }
    }
    output.close();
}
