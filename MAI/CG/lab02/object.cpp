//#include "point.h"
#include "matrix.h"
#include "object.h"
#include <vector>
#include "QPainter"

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
}

void Object::draw(QPainter *painter, vector<double> canvsize){
    int prev;
    for(std::vector< vector <int> >::iterator i = facets.begin(); i != facets.end(); ++i){
        int a = (*i)[0];
        int b = (*i)[1];
        int c = (*i)[2];
        double vectmul = (p[b] - p[a]) * (p[c] - p[a]);
        if (vectmul > 0)
            continue;
        for(std::vector <int>::iterator j = i->begin(); j != i->end(); ++j){
            if (j != i->begin()){
                int now = *j;
                Point an = p[now];
                Point bn = p[prev];
                an.drawline(painter, bn, canvsize);
            }
            prev = *j;
        }
        Point an = p[(*i)[0]];
        Point bn = p[prev];
        an.drawline(painter, bn, canvsize);
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
    return *new Object(pts, facets);
}
