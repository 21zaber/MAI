
#include <iostream>
#include <cmath>

#include "trapezoid.h"

Trapezoid::Trapezoid() : Trapezoid(0, 0, h) {}

Trapezoid::Trapezoid(size_t a, size_t b, size_t h) : a(a), b(b), h(h) {
    std::cout << "Created ";
    this->print();
}

Trapezoid::Trapezoid(std::istream &is) {
    is >> a; 
    is >> b; 
    is >> h; 
    std::cout << "Created ";
    this->print();
}

Trapezoid::Trapezoid(const Trapezoid &orig) {
    std::cout << "Trapezoid copy created" << std::endl;
    a = orig.a;
    b = orig.b;
    b = orig.h;
}

double Trapezoid::square() {
    return h * (double)(a + b) / 2;
}

void Trapezoid::print() {
    std::cout << "Trapezoid, a = " << a << ", b = " << b << ", h = " << h << std::endl;
}

Trapezoid::~Trapezoid() {
    std::cout << "Trapezoid deleted" << std::endl;
}
