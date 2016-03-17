//#include "point.h"
#include "matrix.h"
#include "object.h"
#include <vector>
#include "QPainter"
#include "QPointF"
#include "QColor"
#include "math.h"

Object::Object(){}

Object::Object(vector<Point> pts, vector< vector <int> > fts){
    p.clear();
    for(std::vector<Point>::iterator i = pts.begin(); i != pts.end(); ++i){
        p.push_back(*i);
    }
    facets.clear();
    facets.resize(fts.size());
    int k = 0;
    for(std::vector< vector <int> >::iterator i = fts.begin(); i != fts.end(); ++i, ++k){
        for(std::vector <int>::iterator j = i->begin(); j != i->end(); ++j){
            facets[k].push_back(*j);
        }
    }
    ambient.resize(3, 0.2);
    diffuse.resize(3, 0.5);
    specular.resize(3, 0.3);
    specpow = 30;
}

void Object::setAmbient(double r, double g, double b){
    ambient.clear();
    ambient.push_back(r);
    ambient.push_back(g);
    ambient.push_back(b);
}

void Object::setDiffuse(double r, double g, double b){
    diffuse.clear();
    diffuse.push_back(r);
    diffuse.push_back(g);
    diffuse.push_back(b);
}

void Object::setSpecular(double r, double g, double b, double alpha){
    specular.clear();
    specular.push_back(r);
    specular.push_back(g);
    specular.push_back(b);
    specpow = alpha;
}

QColor Object::_getcolor(Point norm, Point light, Point eye){
    double r = 0, g = 0, b = 0;
    Point half = light + eye;
    half.normalize();

    double diff = max(0.0, (norm ^ light) / norm.mod() / light.mod());
    double spec = pow(max(0.0, (norm ^ half) / norm.mod() / half.mod()), specpow);

    r += ambient[0];
    r += diffuse[0] * diff;
    r += specular[0] * spec;
    r = (r > 1) ? 1 : r;
    r = (r < 0) ? 0 : r;
    r *= 255;

    g += ambient[1];
    g += diffuse[1] * diff;
    g += specular[1] * spec;
    g = (g > 1) ? 1 : g;
    g = (g < 0) ? 0 : g;
    g *= 255;

    b += ambient[2];
    b += diffuse[2] * diff;
    b += specular[2] * spec;
    b = (b > 1) ? 1 : b;
    b = (b < 0) ? 0 : b;
    b *= 255;

    return QColor(r, g, b);
}

void Object::draw(QPainter *painter, Matrix m, vector<double> canvsize){
    for(std::vector< vector <int> >::iterator i = facets.begin(); i != facets.end(); ++i){
        int a = (*i)[0];
        int b = (*i)[1];
        int c = (*i)[2];
        Point n = (p[b] - p[a]) * (p[c] - p[a]);
        Point l(10000, 20000, 0000);
        l = m * l - p[a];
        Point eye(0, 0, -100);
        eye = eye - p[a];
        if (n.z() > 0)
            continue;
        QPointF polygon[i->size()];
        int t = 0;
        for(std::vector <int>::iterator j = i->begin(); j != i->end(); ++j, ++t){
            polygon[t] = QPointF(p[*j].x(), p[*j].y());
        }

        painter->setPen(Qt::NoPen);
        painter->setBrush(_getcolor(n, l, eye));

        painter->drawConvexPolygon(polygon, i->size());
    }
}

void Object::addpoint(double x, double y, double z){
    p.push_back(Point(x, y, z));
}

void Object::addfacet(int a, int b, int c){
    vector<int> q(3);
    q[0] = a;
    q[1] = b;
    q[2] = c;
    facets.push_back(q);
}

void Object::addfacet(int a, int b, int c, int d){
    vector<int> q(4);
    q[0] = a;
    q[1] = b;
    q[2] = c;
    q[3] = d;
    facets.push_back(q);
}

void Object::addfacet(vector<int> p){
    facets.push_back(p);
}

Object Object::operator * (Matrix m){
    vector<Point> pts;
    for (unsigned int i = 0; i < p.size(); ++i){
        pts.push_back(m * p[i]);
    }
    Object *ob = new Object(pts, facets);
    ob->diffuse = diffuse;
    ob->ambient = ambient;
    ob->specpow = specpow;
    ob->specular = specular;
    return *ob;
}
