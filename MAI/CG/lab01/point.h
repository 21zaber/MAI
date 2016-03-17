#ifndef POINT_H
#define POINT_H

#endif // POINT_H

class Point {
private:
public:
    double p[4];

    Point();
    Point(double x, double y, double z);
    Point(double t[4]);

    Point operator * (double a);

    double &x(){return p[0];}
    double &y(){return p[1];}
    double &z(){return p[2];}
    double &w(){return p[3];}
};
