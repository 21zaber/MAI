#include <iostream>
#include "queue.h"
#include "figure.h"
#include "square.h"
#include "rectangle.h"
#include "trapezoid.h"

using namespace std;


shared_ptr<Figure> get() {
    while (true) {
        cout << "Choose figure: 1 - square, 2 - rectangle, 3 - trapezoid. \n";
        int cmd;
        cin >> cmd;
        if (cmd == 1) {
            return shared_ptr<Figure>(new Square(cin));
        } else if (cmd == 2) {
            return shared_ptr<Figure>(new Rectangle(cin));
        } else if (cmd == 3) {
            return shared_ptr<Figure>(new Trapezoid(cin));
        } else {
            continue;
        }
        break;
    }
}

Figure* get1() {
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
    SQueue q;

    for (int i = 0; i < 5; ++i) {
        q.push(get());
        cout << q << endl;
    }

    for (int i = 0; i < 5; ++i) {

        cout << "Poped element: " << q.pop();
        cout << q << endl;
    }
}
