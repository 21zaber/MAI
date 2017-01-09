#include <iostream>
#include <map>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

#define ipr pair<long long, long long>
#define map_type map< ipr, long long >

long long gcd (long long a, long long b) {
    if (a < b) return gcd(b, a);
    if (b == 0) return a;
    return gcd(b, a%b);
}

int main() {
    int n;
    cin >> n;
    map_type v;
    map< ipr, bool > exist;
    for (int i = 0; i < n; ++i) {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        ipr vect = make_pair(c-a, d-b);

        if (vect.first < 0) {
            vect.first *= -1;
            vect.second *= -1;
        }
        
        if (vect.first == 0 and vect.second == 0)
            continue;
        
        long long g = gcd(abs(vect.first), abs(vect.second));
        //cout << g;
        ipr nv = make_pair(vect.first / g, vect.second / g);
        
        if (exist.find(vect) != exist.end() and exist[vect]) {
            if (v.find(nv) == v.end()) {
                v[nv] = 0;
            }
            v[nv] += 1;
           // cout << vect.first << ' ' << vect.second << endl;
            exist[vect] = false;
        } else {
            exist[vect] = true;
        }
    }

    priority_queue<long long> qq;


    for (map_type::iterator i = v.begin(); i != v.end(); ++i) {
        qq.push(i->second);
    }

    long long ans = 0;

    while (qq.size() > 1) {
        long long m1 = qq.top(); qq.pop();
        long long m2 = qq.top(); qq.pop();
        if (m1 > 0 and m2 > 0) {
            ans += 1;
            m1 -= 1;
            m2 -= 1;
        } else {
            break;
        }
                
        if (m1 > 0) {
            qq.push(m1);
        }
        if (m2 > 0) {
            qq.push(m2);
        }
    }

    cout << ans << endl;
}
