#include "queue.h"
#include "square.h"

SQueue::SQueue(const SQueue &orig) {

}

std::ostream& operator<<(std::ostream& os, const SQueue &obj) { 
    SQItem *tmp = obj.head;
    if (tmp == NULL) {
        os << "SQueue is empty\n";
        return os;
    }
    os << "SQueue, size " << obj.sz << ", elements: \n";

    for (int i = 0; i < obj.sz; ++i, tmp = tmp->next()) {
        os << "\t" << *tmp << std::endl;
    }
    return os;
}

void SQueue::push(Square &&s) {
    ++(this->sz);
    SQItem *new_item = new SQItem(s);
    if (this->head == NULL) {
        this->head = new_item;
        new_item->set_prev(new_item);
        return;
    }
    SQItem *tail = this->head->prev();
    tail->insert_after(new_item);
    this->head->set_prev(new_item);
}

Square SQueue::pop() {
    --(this->sz);
    Square s = this->head->get_item();
    SQItem *old_head = this->head;
    this->head = this->head->next();
    delete old_head;
    if (this->sz == 0) {
        this->head = NULL;
    }
    return s;
}

SQueue::~SQueue() {
    SQItem *tmp = this->head, *t;
    while (tmp != NULL) {
        t = tmp;
        tmp = tmp->next();
        delete t;
    }
    std::cout << "SQueue deleted\n";
}
                
