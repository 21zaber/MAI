
#include "queue.h"
#include "rectangle.h"


FQueue::FQueue() : l(0), r(0) {}

FQueue::FQueue(FQueue &orig) {
    size_t sz = (orig.r < orig.l) ? orig.r + QUEUE_SIZE : orig.r;
    for (size_t i = orig.l; i <= sz; ++i) {
        this->push(orig.q[i % QUEUE_SIZE]);
    }
}

std::ostream& operator<<(std::ostream& os, const FQueue &obj) {
    size_t sz = (orig.r < orig.l) ? orig.r + QUEUE_SIZE : orig.r;
    os << "Queue's elements:\n";
    for (size_t i = orig.l; i <= sz; ++i) {
        os << "\t" << orig.q[i %QUEUE_SIZE] << std::endl;
    }

    return os;
}

void FQueue::push(Figure &&f) {
    q[r] = **f;
    *f = *q[r];
    ++r;
}

Figure& FQueue::pop() {
    Figure result = Rectangle();
    if (this->empty()) 
        return result;
    result = q[l++];
    return result;
}

bool FQueue::empty() {
    return l == r;
}

size_t FQueue::size() {
    if (r < l) {
        return QUEUE_SIZE + r - l;
    } else {
        return r - l;
    }
}

FQueue::~FQueue() {

}
