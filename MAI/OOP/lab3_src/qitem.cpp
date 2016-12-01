
#include "qitem.h"

void SQItem::insert_after(SQItem* sqi) {
    if (sqi == NULL) {
        return ;
    }

    if (this->_next != NULL)
        this->_next->_prev = sqi;
    sqi->_next = this->_next;
    sqi->_prev = this;
    this->_next = sqi;
}

std::ostream& operator<<(std::ostream& os, const SQItem &obj) { 
    os  << obj.item;
    //os << ' ' << &obj << ' ' << obj._next << ' ' << obj._prev;
    return os;
}

void SQItem::insert_before(SQItem* sqi) {
    if (sqi == NULL) {
        return ;
    }

    this->_prev->_next = sqi;
    sqi->_prev = this->_prev;
    sqi->_next = this;
    this->_prev = sqi;
}

SQItem::~SQItem() {
    this->_next->_prev = this->_prev;
    this->_prev->_next = this->_next;
}
