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
public:
    Object();
    Object(vector<Point> pts, vector< vector <int> > fts);
    void addpoint(double x, double y, double z);
    void addfacet(int a, int b, int c);
    void addfacet(int a, int b, int c, int d);
    void addfacet(vector<int> p);
    void draw(QPainter *p, vector<double> canvsize);

    Object operator * (Matrix m);
};

#endif // OBJECT_H
