#pragma once

#include "square.h"

class SQItem {
public:
    SQItem():                _next(NULL), _prev(NULL), item()  {};
    SQItem(const Square& s): _next(NULL), _prev(NULL), item(s) {};

    Square get_item() { return this->item; };

    friend std::ostream& operator<<(std::ostream &os, const SQItem &obj);

    void insert_after(SQItem* sqi);
    void insert_before(SQItem* sqi);

    void set_prev(SQItem *prev) { this->_prev = prev; };

    SQItem *next() { return this->_next; };
    SQItem *prev() { return this->_prev; };

    ~SQItem();

private:
    SQItem *_next, *_prev;
    Square item;    
};
