#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

int pow2(int x) {
    return 1 << x;
}

int n;

//vector<int> bits;
bool bits[200];
void get_bits(int mask) {
    memset(bits, 0, sizeof bits);
    for (int i = 0; mask > 0; ++i) {
        bits[i] = mask & 1;
        mask = mask >> 1;
    }
}

int main() {

    cin >> n;

    vector<long long> p = vector<long long>(n);
    vector<long long> p1 = vector<long long>(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
        p1[i] = p[i] / 100;
    }
    
    int best_mask = 0;
    long long best_cost = 10000000 + 1;
    for (int i = 0; i < pow2(n); ++i) {
        //saves result in 'bits'
        get_bits(i);

        long long bonus = 0;
        long long straight_payment = 0;
        
        for (int j = 0; j < n; ++j) {
            if (!bits[j] && bonus == 0) {
                straight_payment = best_cost;
                break;
            }
            if (bits[j]) {
                straight_payment += p[j];
                bonus += p1[j];
            }
            else {
                if (bonus >= p[j]) {
                    bonus -= p[j];
                }
                else {
                    straight_payment += p[j] - bonus;
                    bonus = 0;
                }
            }
        }

       // cout << i << ' ' << straight_payment << endl;
        if (best_cost > straight_payment) {
         //   cout << "new best" << endl;
            best_cost = straight_payment;
            best_mask = i;
        }
    }

    //cout << best_mask << endl;

    //saves result in 'bits'
    get_bits(best_mask);

    //print stuff
    cout << best_cost << endl;
    
    long long bonus = 0;
    for (int j = 0; j < n; ++j) {
        if (bits[j]) {
            cout << p[j] << " + 0" << endl;
            bonus += p[j] / 100;
        }
        else {
            if (bonus >= p[j]) {
                cout << "0 + " << p[j] << endl;
                bonus -= p[j];
            }
            else {
                cout << p[j] - bonus << " + " << bonus << endl;
                bonus = 0;
            }
        }
    }

    return 0;
}
