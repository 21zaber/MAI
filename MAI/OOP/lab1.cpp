
#include "src/figure.h"
#include "src/square.h"
#include "src/rectangle.h"
#include "src/trapezoid.h"

#include <iostream>

using namespace std;

Figure *get() {
    while (true) {
        cout << "Choose figure: 1 - square, 2 - rectangle, 3 - trapezoid. \n";
        int cmd;
        cin >> cmd;
        if (cmd == 1) {
            return new Square(cin);
        } else if (cmd == 2) {
            return new Rectangle(cin);
        } else if (cmd == 3) {
            return new Trapezoid(cin);
        } else {
            continue;
        }
        break;
    }
}

int main() {
    while (true) {
        Figure *f = get();
        cout << "Square: " << f->square() << endl;
    }
}
