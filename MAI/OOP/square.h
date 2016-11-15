#pragma once

#include <cstdlib>
#include <iostream>

#include "figure.h"

class Square : public Figure {
public:
    Square();
    Square(std::istream &is);
    Square(size_t a);
    Square(const Square &orig);

    double square() override;
    void print() override;

    virtual ~Square();
private:  
    size_t a;
};
