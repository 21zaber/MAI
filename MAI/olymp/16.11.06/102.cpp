#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <cstdio>
using namespace std;
 
void discard(set<long long>& s, long long x) {
	set<long long>::iterator it = s.find(x);
	if (it != s.end()) s.erase(it);
}
 
int main() {
	int n;
	cin >> n;
 
	vector<long long> l(n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &l[i]);
	}
 
	sort(l.begin(), l.end(), greater<long long>());
 
	set<long long> s(l.begin(), l.end());
	if (l.size() > 1) {
		discard(s, 1);
	}
 
	for (vector<long long>::iterator it = l.begin(); it != l.end(); ++it) {
		long long i = *it;
		if (s.find(i) == s.end()) continue;
 
        long long tmp = floor(sqrt(i) + 2);
		for (long long k = 2; k < tmp; ++k) {
			if (i % k == 0) {
				discard(s, k);
				discard(s, i / k);
			}
		}
	}
 
	vector<long long> t(s.begin(), s.end());
	sort(t.begin(), t.end());
 
	for (int i = 0; i < t.size(); ++i) {
		printf("%d ", t[i]);
	}
	cout << endl;
 
	return 0;
}
