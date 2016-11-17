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

    friend std::ostream& operator<<(std::ostream &os, const Rectangle &obj);
    friend std::istream& operator>>(std::istream &is, Rectangle &obj);

    Rectangle& operator=(const Rectangle &obj);

    double square() override;
    void print() override;

    virtual ~Rectangle();
private:  
    size_t a;
    size_t b;
};
