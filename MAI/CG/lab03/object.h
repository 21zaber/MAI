#include "vector"
#ifndef OBJECT_H
#define OBJECT_H

#include "point.h"
#include "matrix.h"

using namespace std;

class Object{
private:
    vector<Point> p;
    vector< vector <int> > facets;
    vector<double> ambient;
    vector<double> diffuse;
    vector<double> specular;
    double specpow;

    QColor _getcolor(Point norm, Point light, Point eye);
public:
    Object();
    Object(vector<Point> pts, vector< vector <int> > fts);

    void setAmbient(double r, double g, double b);
    void setDiffuse(double r, double g, double b);
    void setSpecular(double r, double g, double b, double alpha);

    void addpoint(double x, double y, double z);
    void addfacet(int a, int b, int c);
    void addfacet(int a, int b, int c, int d);
    void addfacet(vector<int> p);

    void draw(QPainter *p, Matrix m, vector<double> canvsize);

    Object operator * (Matrix m);
};

#endif // OBJECT_H
