
#include <iostream>
#include <cmath>

#include "rectangle.h"

Rectangle::Rectangle() : Rectangle(0, 0) {}

Rectangle::Rectangle(size_t a, size_t b) : a(a), b(b) {
    std::cout << "Created ";
    this->print();
}

Rectangle::Rectangle(std::istream &is) {
    std::cout << "Enter length of sides: ";
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

std::ostream& operator<<(std::ostream &os, const Rectangle &obj) {
    os << "Rectangle, a = " << obj.a << ", b = " << obj.b << std::endl;
    return os;
}

std::istream& operator>>(std::istream &is, Rectangle &obj) {
    std::cout << "Enter size of sides: ";
    is >> obj.a >> obj.b;
    return is;
}

Rectangle& Rectangle::operator=(const Rectangle &obj) {
    if (this == &obj) return *this;

    std::cout << "Rectangle copied" << std::endl;
    a = obj.a;
    b = obj.b;

    return *this;
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
