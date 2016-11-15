#pragma once

#include <cstdlib>
#include <iostream>

#include "figure.h"

class Rectangle : public Figure {
public:
    Rectangle();
    Rectangle(std::istream &is);
    Rectangle(size_t a, size_t b);
    Rectangle(const Rectangle &orig);

    double square() override;
    void print() override;

    virtual ~Rectangle();
private:  
    size_t a;
    size_t b;
};
