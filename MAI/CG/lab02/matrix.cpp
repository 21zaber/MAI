#include "matrix.h"
#include "math.h"

Matrix::Matrix(){
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (i == j)
                mtrx[i][j] = 1;
            else
                mtrx[i][j] = 0;
}

Matrix::Matrix(double m11, double m12, double m13, double m14,
       double m21, double m22, double m23, double m24,
       double m31, double m32, double m33, double m34,
       double m41, double m42, double m43, double m44){

    mtrx[0][0] = m11; mtrx[0][1] = m12; mtrx[0][2] = m13; mtrx[0][3] = m14;
    mtrx[1][0] = m21; mtrx[1][1] = m22; mtrx[1][2] = m23; mtrx[1][3] = m24;
    mtrx[2][0] = m31; mtrx[2][1] = m32; mtrx[2][2] = m33; mtrx[2][3] = m34;
    mtrx[3][0] = m41; mtrx[3][1] = m42; mtrx[3][2] = m43; mtrx[3][3] = m44;
}

Matrix::Matrix(double t[4][4]){
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            mtrx[i][j] = t[i][j];
        }
    }
}

Point Matrix::operator * (Point p){
    double t[4];
    for (int i = 0; i < 4; i++){
        t[i] = 0;
        for (int j = 0; j < 4; j++){
            t[i] += mtrx[i][j] * p.p[j];
        }
    }
    return Point(t);
}

Matrix Matrix::operator * (Matrix m){
    double t[4][4];
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++){
            t[i][j] = 0;
            for (int k = 0; k < 4; k++){
                t[i][j] += mtrx[i][k] * m.mtrx[k][j];
            }
        }
    }
    return Matrix(t);
}

void Matrix::print(std::ofstream &fout){
    fout << "******";
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            fout << mtrx[i][j] << ' ';
}

Matrix Matrix::rotateX(double a){
    double s = sin(a), c = cos(a);
    return Matrix(1,  0, 0, 0,
               0,  c, s, 0,
               0, -s, c, 0,
               0,  0, 0, 1);
}

Matrix Matrix::rotateY(double a){
    double s = sin(a), c = cos(a);
    return Matrix(c,  0, s, 0,
                  0,  1, 0, 0,
                  -s, 0, c, 0,
                  0,  0, 0, 1);
}

Matrix Matrix::rotateZ(double a){
    double s = sin(a), c = cos(a);
    return Matrix(c,  s, 0, 0,
                  -s, c, 0, 0,
                  0,  0, 1, 0,
                  0,  0, 0, 1);
}

Matrix Matrix::move(Point p){
    return Matrix(1, 0, 0, p.x(),
                  0, 1, 0, p.y(),
                  0, 0, 1, p.z(),
                  0, 0, 0, 1);
}
