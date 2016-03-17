#ifndef MATRIX_H
#define MATRIX_H

#include "point.h"
#include "fstream"




class Matrix{
public:
    double mtrx[4][4];

    Matrix();
    Matrix(double m11, double m12, double m13, double m14,
           double m21, double m22, double m23, double m24,
           double m31, double m32, double m33, double m34,
           double m41, double m42, double m43, double m44);
    Matrix(double t[4][4]);
    Point operator * (Point p);
    Matrix operator * (Matrix m);
    Matrix rotateX(double a);
    Matrix rotateY(double a);
    Matrix rotateZ(double a);
    Matrix move(Point p);
    void print(std::ofstream &);
};

#endif // MATRIX_H
