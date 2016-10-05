#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <queue>
using namespace std;

const long double inf = 1000000000;

vector<int> used;
vector<long double> way;
vector<pair<int, int> > v;
int n, x, y;

long double sqr(int a) {
	return a * a;
};
long double dist(int a, int b) {
	return sqrt((long double)(sqr(v[a].first - v[b].first) + sqr(v[a].second - v[b].second)));
};	

int main()
{
	freopen("unionday.in", "r", stdin);
	freopen("unionday.out", "w", stdout);

	cin >> n;

	used.resize(n, 0);
	way.resize(n, inf);
	way[0] = 0;

	for (int i = 0; i < n; i++){
		cin >> x >> y;
		v.push_back(make_pair(x, y));
	}

	int tmpv = 0;
	for (int i = 0; i < n; i ++){
		tmpv = -1;		
		for (int j = 0; j < n; j ++){
			if (((tmpv == -1) || (way[tmpv] > way[j])) && !used[j]) {
				tmpv = j;
			};
		};		
		used[tmpv] = 1;		
		for (int j = 0; j < n; j ++){
			if ((j != tmpv) && (!used[j])) {
				way[j] = min(way[j], dist(j, tmpv));
			};
		};
	};
	long double ans = 0;
	for (int i = 0; i < n; i++) {
		ans += way[i];
	};
	cout.precision(20);
	cout << ans;
}

