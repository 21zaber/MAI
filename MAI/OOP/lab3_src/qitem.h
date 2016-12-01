#pragma once

#include "square.h"
#include "figure.h"
#include <memory>

class SQItem {
public:
    SQItem():                _next(NULL), _prev(NULL), item()  {};
    SQItem(const std::shared_ptr<Figure>& f): _next(NULL), _prev(NULL), item(f) {};

    std::shared_ptr<Figure> get_item() { return this->item; };

    friend std::ostream& operator<<(std::ostream &os, const SQItem &obj);

    void insert_after(SQItem* sqi);
    void insert_before(SQItem* sqi);

    void set_prev(SQItem *prev) { this->_prev = prev; };

    SQItem *next() { return this->_next; };
    SQItem *prev() { return this->_prev; };

    ~SQItem();

private:
    SQItem *_next, *_prev;
    std::shared_ptr<Figure> item;
};
