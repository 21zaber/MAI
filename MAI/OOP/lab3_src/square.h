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

    friend std::ostream& operator<<(std::ostream &os, const Square &obj);
    friend std::istream& operator>>(std::istream &is, Square &obj);

    Square& operator=(const Square &obj);

    double square() override;
    void print() override;

    virtual ~Square();
private:  
    size_t a;
};
