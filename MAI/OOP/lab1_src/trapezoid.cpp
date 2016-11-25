
#include <iostream>
#include <cmath>

#include "trapezoid.h"

Trapezoid::Trapezoid() : Trapezoid(0, 0, h) {}

Trapezoid::Trapezoid(size_t a, size_t b, size_t h) : a(a), b(b), h(h) {
    std::cout << "Created ";
    this->print();
}

Trapezoid::Trapezoid(std::istream &is) {
    std::cout << "Enter length of bases: ";
    is >> a; 
    is >> b; 
    std::cout << "Enter hight: ";
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

std::ostream& operator<<(std::ostream &os, const Trapezoid &obj) {
    os << "Trapezoid, a = " << obj.a << ", b = " << obj.b << ", h = " << obj.h << std::endl;
    return os;
}

std::istream& operator>>(std::istream &is, Trapezoid &obj) {
    std::cout << "Enter sizes of bases: ";
    is >> obj.a >> obj.b;
    std::cout << "Enter height: ";
    is >> obj.h;
    return is;
}

Trapezoid& Trapezoid::operator=(const Trapezoid &obj) {
    if (this == &obj) return *this;

    std::cout << "Trapezoid copied" << std::endl;
    a = obj.a;
    b = obj.b;
    h = obj.h;

    return *this;
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
