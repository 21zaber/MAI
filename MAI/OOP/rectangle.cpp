
#include <iostream>
#include <cmath>

#include "rectangle.h"

Rectangle::Rectangle() : Rectangle(0, 0) {}

Rectangle::Rectangle(size_t a, size_t b) : a(a), b(b) {
    std::cout << "Created ";
    this->print();
}

Rectangle::Rectangle(std::istream &is) {
    is >> a; 
    is >> b; 
    std::cout << "Created ";
    this->print();
}

Rectangle::Rectangle(const Rectangle &orig) {
    std::cout << "Rectangle copy created" << std::endl;
    a = orig.a;
    b = orig.b;
}

double Rectangle::square() {
    return a * b;
}

void Rectangle::print() {
    std::cout << "Rectangle, a = " << a << ", b = " << b << std::endl;
}

Rectangle::~Rectangle() {
    std::cout << "Rectangle deleted" << std::endl;
}
