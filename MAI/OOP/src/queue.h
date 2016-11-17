#pragma once

#include <iostream>

#include "figure.h"

#define QUEUE_SIZE 100

class FQueue {
public:
    FQueue();
    FQueue(FQueue &orig);

    friend std::ostream& operator<<(std::ostream& os, const FQueue &obj);

    void push(Figure &&f);
    Figure& pop();

    bool empty();
    size_t size();

    ~FQueue();
private:
    size_t l, r;
    Figure& q[QUEUE_SIZE];
};
