#pragma once

#include <iostream>
#include <memory>

class Figure {
public:
    friend std::ostream& operator<<(std::ostream &os, const std::shared_ptr<Figure>& f);
    virtual friend std::ostream& std::ostream::operator<<(std::ostream &os, const Figure& f);
    virtual double square() = 0;
    virtual void print() = 0;
};

