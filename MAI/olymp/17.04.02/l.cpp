#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <cstdlib>
#include <stdio.h>

using namespace std;

int idx = 0;

class comp_t {
public:
    set<int> h;
    set<int> v;
    int sz; 
    int id;   

    comp_t() : h(), v(), sz(0), id(idx++) {};
};

map<int, comp_t *> h;
map<int, comp_t *> v;


void merge(comp_t *a, comp_t *b) {
    if (b == NULL or a == b) {
        return;
    }
    if (rand() % 2 == 0){
        comp_t *c = a;
        a = b;
        b = c;
    }

    for (set<int>::iterator i = b->h.begin(); i != b->h.end(); ++i) {
        a->h.insert(*i);
        h[*i] = a;
    }

    for (set<int>::iterator i = b->v.begin(); i != b->v.end(); ++i) {
        a->v.insert(*i);
        v[*i] = a;
    }
    a->sz += b->sz;
}

void add(int x, int y) {
    comp_t *a = NULL, *b = NULL;
    if (h.find(x) != h.end()) {
        a = h[x];
    } else {
        a = new comp_t;
    }
    if (v.find(y) != v.end()) {
        b = v[y];
    }
    a->h.insert(x);
    a->v.insert(y);
    a->sz += 1;
    h[x] = a;
    v[y] = a;
    merge(a, b);
}

void test() {
    cout << "hor" << endl;
    for (map<int, comp_t *>::iterator i = h.begin(); i != h.end(); ++i) {
        cout << i->first+1 << ' ' << i->second->id << ' ' << i->second->sz << endl;
    }
    cout << "ver" << endl;
    for (map<int, comp_t *>::iterator i = v.begin(); i != v.end(); ++i) {
        cout << i->first+1 << ' ' << i->second->id << ' ' << i->second->sz << endl;
    }
    cout << "\n\n\n\n";
}


int main() {
    ios_base::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;

    bool s[n][m]; 

    vector<pair<int, int> > arr(n*m);
    int number = 0;
    string ss;

    cout << "0\n";

    for (int i = 0; i < n; ++i) {
        cin >> ss;
        for (int j = 0; j < m; ++j) {
            char c = ss[j];
            s[i][j] = false;
            if (c == '+') {
                add(i, j);
 //               arr[number++] = make_pair(i, j);
                s[i][j] = true;
            }
        }
    }

 // cout << "1\n";
 // int len = number-1;
 // 
 // for (int i = 0; i < 100000; i++) {
 //     int a = rand() % len, b = rand() % len;
 //     if (a != b) {
 //         int c = arr[a].first, d = arr[a].second;
 //         arr[a].first = arr[b].first;
 //         arr[a].second = arr[b].second;
 //         arr[b].first = c;
 //         arr[b].second = d;
 //     }
 // }
 //
 //
 // for (int i = 0; i < len; ++i){
 //     add(arr[i].first, arr[i].second);
 // }

    cout << "2\n";

    comp_t *m1 = NULL, *m2 = NULL;
    for (map<int, comp_t *>::iterator i = h.begin(); i != h.end(); ++i) {
        comp_t *a = i->second;
        if (m1 == a or m2 == a) continue;
        if (m1 == NULL) {
            m1 = i->second;
            continue;
        }
        if (m2 == NULL and i->second != m1) {
            m2 = i->second;
            continue;
        }
        if (a->sz > m1->sz and a != m1 and a != m2) {
            m2 = m1;
            m1 = a;
            continue;
        }
        if (a->sz > m2->sz and a != m1 and a != m2) {
            m2 = a;
            continue;
        }
    }

    for (map<int, comp_t *>::iterator i = v.begin(); i != v.end(); ++i) {
        comp_t *a = i->second;
        if (m1 == a or m2 == a) continue;
        if (m1 == NULL) {
            m1 = i->second;
            continue;
        }
        if (m2 == NULL and a != m1) {
            m2 = i->second;
            continue;
        }
        if (a->sz > m1->sz and a != m1 and a != m2) {
            m2 = m1;
            m1 = a;
            continue;
        }
        if (a->sz > m2->sz and a != m1 and a != m2) {
            m2 = a;
            continue;
        }
    }

    //cout << "ans " << m1->id  << ' ' << m1->sz << endl;

    int ans = 0, x = 0, y = -1;
    if (m1 != NULL) {
        ans += m1->sz;
        x = *(m1->h.begin());
    }
    if (m2 != NULL) {
        ans += m2->sz;
        y = *(m2->v.begin());
    } else {
        for (int i = 0; i < n; ++i) {
            if (y != -1) {
                break;
            }
            for (int j = 0; j < m; ++j) {
                if (s[i][j] == false) {
                    if ((h.find(i) != h.end()) or (v.find(j) != v.end())) {
                        x = i;
                        y = j;
                    }
                }
            }
        }    
    }
    if (ans == n * m) {
        ans = 0;
    }
    cout << ans << endl;
    if (ans != 0) {
        cout << x+1 << ' ' << y+1 << endl;
    }    
}
