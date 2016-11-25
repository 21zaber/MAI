#include <iostream>
#include "square.h"
#include "queue.h"

using namespace std;

int main() {
    SQueue q;

    for (int i = 0; i < 5; ++i) {
        q.push(Square(cin));
        cout << q << endl;
    }

    for (int i = 0; i < 5; ++i) {

        cout << "Poped element: " << q.pop() << endl;
        cout << q << endl;
    }
}
