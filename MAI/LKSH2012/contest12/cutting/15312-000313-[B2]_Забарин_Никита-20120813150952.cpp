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

int n, m, k, a, b;
string s;
vector<int> king, r;
vector<bool> ans;
vector<pair<string, pts> > cmd;

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

void ask (int a, int b, int i){
	ans[i] = (get(a) == get(b));
};


int main()
{
	freopen("cutting.in", "r", stdin);
	freopen("cutting.out", "w", stdout);

	cin >> n >> m >> k;

	king.resize(n);
	ans.resize(k);
	r.resize(n);

	for (int i = 0; i < n; i++){
		king[i] = i;
		r[i] = 1;
	};

	int a, b;
	for (int i = 0; i < m; i ++){
		cin >> a >> b;
	};
	pts t;
	for (int i = 0; i < k; i ++){
		cin >> s >> a >> b;
		t.x = a - 1;
		t.y = b - 1;
		cmd.push_back(make_pair(s, t));
	};
	int j = 0;
	for (int i = k - 1; i > -1; i --){
		if (cmd[i].first == "cut") {
			un(cmd[i].second.x, cmd[i].second.y);
		};
		if (cmd[i].first == "ask") {
			ask(cmd[i].second.x, cmd[i].second.y, j);
			j++;
		};
	};
	for (int i = j - 1; i > -1; i--){
		if (ans[i]){
			cout << "YES" << "\n";
		} else {
			cout << "NO" << "\n";
		};
	};
	return 0;
}

