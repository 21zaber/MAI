
#include "figure.h"


std::ostream& operator<<(std::ostream &os, const std::shared_ptr<Figure>& f) {
    os << *f;
    return os;
}
