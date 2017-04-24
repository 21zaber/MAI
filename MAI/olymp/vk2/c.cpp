#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <stdlib.h> 

using namespace std;

set<int> learn;
vector<int> ans;
vector<int> need;
vector<vector <int> > edgs;
vector<bool> used;
queue<int> q;

void bfs(int v, int start) {
    if (learn.find(v) != learn.end()) {
        return;
    }
    learn.insert(v);
    ans.push_back(v);
    for (int i = 0; i < edgs[v].size(); ++i) {
        int to = edgs[v][i];
        if (!used[to]) {
            used[to] = true;
            bfs(to, start);
            used[to] = false;
        } else {
            cout << "-1\n";
            exit(0);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < k; ++i) {
        int t;
        cin >> t;
        need.push_back(t-1);
    }    
    edgs.resize(n, vector<int>());
    for (int i = 0; i < n; ++i) {
        int t;
        cin >> t;
        for (int j = 0; j < t; ++j) {
            int tt;
            cin >> tt;
            //edgs[tt].push_back(i);
            edgs[i].push_back(tt-1);
        }
    }
  //for (int i = 0; i < n; ++i) {
  //    cout << i << ": ";
  //    for (int j = 0; j < edgs[i].size(); ++j) {
  //        cout << edgs[i][j] << ' ';
  //    }
  //    cout << endl;
  //}
    for (int i = 0; i < k; ++i) {
        used.resize(n, false);
        used[need[i]] = true;
        bfs(need[i], need[i]);
        continue;
		while (!q.empty()) {
			bfs(q.front(), need[i]);
			q.pop();
		}
    }

    cout << ans.size() << endl;
    for (int i = 0; i < ans.size(); ++i) {
        cout << ans[ans.size()-1-i]+1 << ' ';
    }
    cout << endl;
}
