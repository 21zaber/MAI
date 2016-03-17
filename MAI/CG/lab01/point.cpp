#include "point.h"

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


