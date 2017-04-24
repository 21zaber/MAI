#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string s;
    cin >> s;

    int n = s.size();


    vector<int> m(n, 0), h(n, 0);

    for (int i = 0; i < n; ++i) {
        if (i == 0) {
            if (s[i] == 'M') {
                m[0] = 1;
            } else if (s[i] == 'H') {
                h[0] = 1;
            }
        } else {
            h[i] = h[i-1];
            m[i] = m[i-1];
            if (s[i] == 'M') {
                m[i] += 1;
            } else if (s[i] == 'H') {
                h[i] += 1;
            } else {
                if (h[i] < 1) {
                    m[i] = 0;
                    h[i] = 0;
                } else {
                    h[i] -= 1;
                }
            }
        }
    }

    int mx = 0;
    for (int i = 0; i < n; ++i) {
        if (m[i] > mx) {
            mx = m[i];
        }
    }

    cout << mx << endl;
}
