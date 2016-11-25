#pragma once

#include <iostream>
#include "square.h"
#include "qitem.h"

class SQueue {
public:
    SQueue(): head(NULL), sz(0) {};
    SQueue(const SQueue &orig);

    friend std::ostream& operator<<(std::ostream& os, const SQueue &obj);

    void push(Square &&s);
    Square pop();

    bool empty() { return (this->sz == 0); };
    size_t size() { return this->sz; };

    ~SQueue();
private:
    SQItem *head;
    size_t sz;
};
