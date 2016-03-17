#ifndef CANVAS_H
#define CANVAS_H
#include "object.h"
#include "vector"
#include "matrix.h"
#include "qpainter.h"

class Canvas{
public:
    Canvas();
    Canvas(QPainter &p, double x, double y, double canvwidth, double canvheight);
    Canvas(QPainter &p, double width, double height);

    void setMatrix(Matrix m);
    void setSize(double width, double height);
    void setPainter(QPainter &p);

    void addObject(Object object);
    void clearObjects();

    void drawAll();
private:
    void _clear();
    void _drawXYZ();
    vector<double> _canvsSize();

    QPainter *painter;
    vector<Object> objects;
    Matrix matrix;
    double minx, miny, maxx, maxy;
};

#endif // CANVAS_H
