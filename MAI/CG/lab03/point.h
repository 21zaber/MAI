#ifndef POINT_H
#define POINT_H

#include "QPainter"
#include "vector"

using namespace std;

class Point {
private:
public:
    double p[4];

    Point();
    Point(double x, double y, double z);
    Point(double t[4]);

    Point operator * (double a);
    Point operator - (const Point b);
    Point operator + (const Point b);
    Point operator * (const Point b);
    double operator ^ (const Point b);

    double mod();
    void normalize();
    void drawline(QPainter *p, Point b, vector<double> canvsize);
    void drawdottedline(QPainter *p, Point b, vector<double> canvsize);

    double &x(){return p[0];}
    double &y(){return p[1];}
    double &z(){return p[2];}
    double &w(){return p[3];}
};

#endif // POINT_H
