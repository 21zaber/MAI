#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <stack>
#include <string>
using namespace std;

const int inf = 1000000000;

struct pts{
	int x, y;
};

int n, m, k, a, b, l, f;
string s;
vector<int> king, r;
vector<bool> used;
long long ans;
vector<pair<int, pair<int, int> > > edges;

int get (int v){
	if (king[v] == v) {
		return v;	
	};
	return get(king[v]);
};

void un (int a, int b){
	int t1 = get(a);
	int t2 = get(b);

	if (r[t1] <= r[t2]){
		swap(t1, t2);
	};
	king[t2] = t1;
	r[t1] = max(king[t1], king[t2] + 1);
};


int main()
{
	freopen("mst.in", "r", stdin);
	freopen("mst.out", "w", stdout);

	cin >> n >> m;

	king.resize(n);
	r.resize(n);
	used.resize(m);
	ans = 0;

	for (int i = 0; i < n; i++){
		king[i] = i;
		r[i] = 1;
	};
	for (int i = 0; i < m; i ++){
		cin >> a >> b >> l;
		edges.push_back(make_pair(l, make_pair(a - 1, b - 1)));
	};
	sort(edges.begin(), edges.end());
	used[0] = 1;
	f = 1;
	un(edges[0].second.first, edges[0].second.second);
	int i = 1;
	while ((f != n - 1) && (i < m)) {
		if (!used[i]) {
			if (get(edges[i].second.first) != get(edges[i].second.second)) {
				un(edges[i].second.first, edges[i].second.second);
				used[i] = 1;
				f++;
			};
		};
		i++;
	};
	for (int i = 0; i < m; i++) {
		if (used[i] == 1) {
			ans += edges[i].first;
		}
	}
	
	cout << ans;
	
	return 0;
};

