#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

const int inf = 1000000000;

int n, m, s, f, a, b, c, i, l, vto;
vector<int> way, used;
vector< vector< pair<int, int> > > mas;
priority_queue< pair<int, int> > h;

int main()
{
	//freopen("C:\Programming\lksh 2012\011\a06\Debug\tmp.in", "r", stdin);
	//freopen("C:\Programming\lksh 2012\011\a06\Debug\tmp.out", "w", stdout);

	freopen("distance.in", "r", stdin);
	freopen("distance.out", "w", stdout);

	cin >> n >> m >> s >> f;

	s--;
	f--;

	mas.resize(n);
	used.resize(n);
	way.resize(n, inf);

	way[s] = 0;
	for (i = 0; i < m; i++){
		cin >> a >> b >> c;
		a += -1;
		b += -1;
		mas[a].push_back(make_pair(b, c));
		mas[b].push_back(make_pair(a, c));
	}
	h.push(make_pair(0, s));
	int v = 0;
	while (!h.empty()) {
		v = h.top().second;
		h.pop();
		if (used[v]) {
			continue;		
		}
		used[v] = 1;

		for (i = 0; i < mas[v].size(); i++){
			vto = mas[v][i].first;
			l = mas[v][i].second;
			if (way[vto] > way[v] + l) {
				way[vto] = way[v] + l;
				h.push(make_pair(-way[vto], vto));
			}
		}
	}
	if (way[f] == inf){
		cout << -1;
	} else {
		cout << way[f];
	}
	return 0;
}

