

#include <iostream>




using namespace std;

int main() {
    int n, l, k;
    cin >> l >> n >> k;
    for (int i = 0; i < l; ++i) {
        int s = n / k;
        if (n % k > 2) {
            ++s;
        } else {
            n -= n % k;
        }
        s = (2 * s) - 1;
        if (s < 1) s = 1;
        n -= s;
    }
    if (n < 0) {
        cout << "0\n";
    } else {
        cout << n << endl;
    }
}
