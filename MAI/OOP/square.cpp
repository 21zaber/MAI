
#include <iostream>
#include <cmath>

#include "square.h"

Square::Square() : Square(0) {}

Square::Square(size_t a) : a(a) {
    std::cout << "Created ";
    this->print();
}

Square::Square(std::istream &is) {
    is >> a; 
    std::cout << "Created ";
    this->print();
}

Square::Square(const Square &orig) {
    std::cout << "Square copy created" << std::endl;
    a = orig.a;
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

