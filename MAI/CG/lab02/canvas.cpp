#include "canvas.h"
#include "qpainter.h"

Canvas::Canvas(){
    painter = NULL;
    minx = 0; miny = 0;
    maxx = 0; maxy = 0;
}

Canvas::Canvas(QPainter &p, double x, double y, double canvwidth, double canvheight){
    minx = x;
    miny = y;
    maxx = canvwidth  + x;
    maxy = canvheight + y;
    painter = &p;
}

Canvas::Canvas(QPainter &p, double width, double height){
    setSize(width, height);
    painter = &p;
}

void Canvas::setMatrix(Matrix m){
    matrix = m;
}

void Canvas::setSize(double width, double height){
    minx = 15;
    miny = 15;
    maxx = width - 190;
    maxy = height - 35;
}

void Canvas::setPainter(QPainter &p){
    painter = &p;
}

void Canvas::addObject(Object object){
    objects.push_back(object);
}

void Canvas::clearObjects(){
    objects.clear();
}

void Canvas::drawAll(){
    _drawXYZ();
    vector<double> canvsize = _canvsSize();
    for (unsigned int i = 0; i < objects.size(); ++i){
        Object ob = objects[i] * matrix;
        ob.draw(painter, canvsize);
        //objects[i].draw(painter, matrix, false, canvsize);
    }
}

vector<double> Canvas::_canvsSize(){
    vector<double> t;// = (minx, miny, maxx, maxy);
    t.push_back(minx);
    t.push_back(miny);
    t.push_back(maxx);
    t.push_back(maxy);
    return t;
}

void Canvas::_drawXYZ(){
    painter->fillRect(minx, miny, maxx - minx, maxy - miny, Qt::white);
    Point center((minx + maxx) / 2, (miny + maxy) / 2, 0);
    double ln = std::min((maxx - minx), (maxy - miny)) / 3;
    Point ox(ln, 0, 0), oy(0, ln, 0), oz(0, 0, ln);
    ox = matrix * ox;
    oy = matrix * oy;
    oz = matrix * oz;
    painter->setPen(Qt::red);
    painter->drawLine(center.x(), center.y(), ox.x(), ox.y());
    painter->setPen(Qt::blue);
    painter->drawLine(center.x(), center.y(), oy.x(), oy.y());
    painter->setPen(Qt::green);
    painter->drawLine(center.x(), center.y(), oz.x(), oz.y());
    painter->setPen(Qt::black);
}
