#include <iostream>

using namespace std;

#define BIT_CNT 62

int main() {
    long long n, s, a = 0;
    ios_base::sync_with_stdio(false);

    cin >> n >> s;

    long long x;
        
    int arr[70];
    for (int i = 0; i < BIT_CNT; ++i) arr[i] = 0;

    for (int i = 0; i < n; ++i) {
        cin >> x;
        for (long long j = 0, t = 1; j < BIT_CNT; ++j, t <<= 1) {
            if ((x & t) > 0) {
                ++arr[j];
            }
        }
    }

    int r = 0;

  //for (int i = 0; i < BIT_CNT; ++i) {
  //    cout << arr[i] << ' ';
  //}
  //
  //cout << endl;

    for (long long i = 0, t = 1; i < BIT_CNT; ++i, t <<= 1) {
       // cout << i << " arr " << arr[i] << " r " << arr[i] << " s " << ((s & t) > 0) << endl; 
        if (((s & t) > 0) != ((arr[i] + r) & 1)) {
        //    cout << i << ' ' << 1 << endl;
            if (((s & t) > 0) == ((n - arr[i] + r) & 1)) {
                a += t;
                arr[i] = n - arr[i];
       //         cout << "a " << a << endl;
            } else {
                cout << -1 << endl;       
                return 0;
            }
        }
        r = arr[i] + r;
        r >>= 1;
    }
    cout << a << endl;
}
