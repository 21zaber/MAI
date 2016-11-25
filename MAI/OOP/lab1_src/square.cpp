
#include <iostream>
#include <cmath>

#include "square.h"

Square::Square() : Square(0) {}

Square::Square(size_t a) : a(a) {
    std::cout << "Created ";
    this->print();
}

Square::Square(std::istream &is) {
    std::cout << "Enter length of side: ";
    is >> a; 
    std::cout << "Created ";
    this->print();
}

Square::Square(const Square &orig) {
    std::cout << "Square copy created" << std::endl;
    a = orig.a;
}

std::ostream& operator<<(std::ostream &os, const Square &obj) {
    os << "Square, a = " << obj.a << std::endl;
    return os;
}

std::istream& operator>>(std::istream &is, Square &obj) {
    std::cout << "Enter size of side: ";
    is >> obj.a;
    return is;
}

Square& Square::operator=(const Square &obj) {
    if (this == &obj) return *this;

    std::cout << "Square copied" << std::endl;
    a = obj.a;

    return *this;
}

double Square::square() {
    return a * a;
}

void Square::print() {
    std::cout << "Square, a = " << a << std::endl;
}

Square::~Square() {
    std::cout << "Square deleted" << std::endl;
}

