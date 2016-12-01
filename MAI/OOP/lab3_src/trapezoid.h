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

    friend std::ostream& operator<<(std::ostream &os, const Trapezoid &obj);
    friend std::istream& operator>>(std::istream &is, Trapezoid &obj);

    Trapezoid& operator=(const Trapezoid &obj);

    double square() override;
    void print() override;

    virtual ~Trapezoid();
private:  
    size_t a;
    size_t b;
    size_t h;
};
