#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

const long long inf = 1000000000000000000;

class Vect {
public:
	long long x, y;
	Vect (){};
	Vect (long long a, long long b){
		x = a;
		y = b;
	};	
	long double l (){
		return sqrt((long double)(x * x + y * y));
	};
	long double operator * (Vect b){
		return x * b.y - y * b.x;
	};
	Vect operator + (Vect b){
		Vect v;
		v.x = x + b.x;
		v.y = y + b.y;
		return v;
	};

};

Vect makevect (Vect a, Vect b){
	Vect v;
	v.x = b.x - a.x;
	v.y = b.y - a.y;
	return v;
};
Vect readvect (){
	Vect v;
	long long x, y;
	cin >> x >> y;
	v.x = x;
	v.y = y;
	return v;
};

Vect v0, v;
int n, m, k, c;
vector<Vect> mas;

int cmpr(Vect v1, Vect v2) {
	return (v1 * v2) >= 0;
};

int bin_search(int l, int r, Vect v) {
	while (r - l > 1) {
		int m = (l + r) / 2;		
		if (cmpr(mas[m], v)) {
			l = m;
		} else {
			r = m;
		};
	};
	
	if (cmpr(mas[r], v)) {
		return r;
	};
	
	if (cmpr(mas[l], v)) {
		return l;
	};
}

int main() {
	freopen("theodore.in", "r", stdin);
	freopen("theodore.out", "w", stdout);
	
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		Vect v = readvect();
		
		if (i == 0) {
			v0 = v;
		} else {
			mas.push_back(makevect(v0, v));
		};
	};

	int c = 0;
	
	for (int i = 0; i < m; i++) {
		Vect v = readvect();
		
		if ((mas[0] * makevect(v0, v)) >= 0 && (makevect(v0, v) * mas[mas.size() - 1]) >= 0) {
			int d = bin_search(0, mas.size() - 1, makevect(v0, v));			
			if (d >= 0) {
				if (d == mas.size() - 1) {
					if (mas[d].l() >= makevect(v0, v).l()) {
						c++;
					};
				} else {
					if ((makevect(mas[d] + v0, mas[d + 1] + v0) * makevect(mas[d] + v0, v)) >= 0) {
						c++;
					};
				};
			};
		};
	};
	
	if (c >= k) {
		cout << "YES";
	} else {
		cout << "NO";
	};
};