#include "point.h"
#include "QPainter"
#include "math.h"

Point::Point() {
    p[0] = 0;
    p[1] = 0;
    p[2] = 0;
    p[3] = 1;
}

Point::Point(double x, double y, double z) {
    p[0] = x;
    p[1] = y;
    p[2] = z;
    p[3] = 1;
}

Point::Point(double t[4]) {
    for (int i = 0; i < 4; i++)
        p[i] = t[i];
}

Point Point::operator * (double a){
    if (a == 0)
        return Point(p);
    for (int i = 0; i < 3; i++){
        p[i] *= a;
    }
    return Point(p);
}

Point Point::operator - (const Point b){
    double p1[4];
    for (int i = 0; i < 4; ++i){
        p1[i] = b.p[i] - p[i];
    }
    return Point(p1);
}

Point Point::operator + (const Point b){
    double p1[4];
    for (int i = 0; i < 3; ++i){
        p1[i] = p[i] + b.p[i];
    }
    return Point(p1);
}

Point Point::operator * (const Point b){
    //{aybz - azby; azbx - axbz; axby - aybx}
    return *new Point(p[1] * b.p[2] - p[2] * b.p[1],
                      p[2] * b.p[0] - p[0] * b.p[2],
                      p[0] * b.p[1] - p[1] * b.p[0]);
}

double Point::mod(){
    return sqrt(p[0] * p[0] + p[1] * p[1] + p[2] * p[2]);
}

void Point::normalize(){
    double m = mod();
    p[0] /= m;
    p[1] /= m;
    p[2] /= m;
}

double Point::operator ^ (const Point b){
    double ans = 0;
    for (int i = 0; i < 3; ++i){
        ans += p[i] * b.p[i];
    }
    if (ans < 0) return 0;
    return ans;
}

void Point::drawline(QPainter *p, Point b, vector<double> canvsize){
    double minx = canvsize[0];
    double miny = canvsize[1];
    double maxx = canvsize[2];
    double maxy = canvsize[3];
    if (x() > minx and b.x() > minx and
        x() < maxx and b.x() < maxx and
        y() > miny and b.y() > miny and
        y() < maxy and b.y() < maxy)
        p->drawLine(x(), y(), b.x(), b.y());
}
//drawdottedline

void Point::drawdottedline(QPainter *p, Point b, vector<double> canvsize){
    p->setPen(Qt::DashDotDotLine);

    this->drawline(p, b, canvsize);

    p->setPen(Qt::SolidLine);
}

