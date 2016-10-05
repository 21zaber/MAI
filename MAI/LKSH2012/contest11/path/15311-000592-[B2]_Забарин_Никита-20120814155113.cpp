#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long inf = (long long)9e18;

vector< pair< pair <int, int>, long long> > mas;
vector<long long> ways;
vector< vector<int> > arr;
vector<int> used2, used;
int n, m, s;
long long k;


void dfs(int v) {
	used[v] = true;	
	for (int i = 0; i < arr[v].size(); i++) {
		if (!used[arr[v][i]]) {
			dfs(arr[v][i]);
		};
	};
};

int main() {
	freopen("path.in", "r", stdin);
	freopen("path.out", "w", stdout);
	
	cin >> n >> m >> s;
	
	s--;
	ways.resize(n, inf);
	used2.resize(n);
	used.resize(n, false);
	arr.resize(n);
	int l, j;
	for (int i = 0; i < m; i++) {
		cin >> l >> j >> k;		
		l--;
		j--;
		mas.push_back(make_pair(make_pair(l, j), k));
		arr[l].push_back(j);
	};
	
	ways[s] = 0;
	
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j < m; j++) {			
			if (ways[mas[j].first.first] != inf) {
				if (ways[mas[j].first.second] > ways[mas[j].first.first] + mas[j].second) {
					ways[mas[j].first.second] = ways[mas[j].first.first] + mas[j].second;					
					if (i == n) {
						used2[mas[j].first.second] = true;
					};
				};
			};
		};
	};
	
	for (int i = 0; i < n; i++) {
		if (used2[i]) {
			dfs(i);
		};
	};	
	for (int i = 0; i < n; i++) {
		if (used[i]) {
			cout << '-' << "\n";
		} else if (ways[i] == inf) {
			cout << '*' << "\n";
		} else {
			cout << ways[i] << "\n";
		};
	};
};
