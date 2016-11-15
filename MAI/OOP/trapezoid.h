#pragma once

#include <cstdlib>
#include <iostream>

#include "figure.h"

class Trapezoid : public Figure {
public:
    Trapezoid();
    Trapezoid(std::istream &is);
    Trapezoid(size_t a, size_t b, size_t h);
    Trapezoid(const Trapezoid &orig);

    double square() override;
    void print() override;

    virtual ~Trapezoid();
private:  
    size_t a;
    size_t b;
    size_t h;
};
