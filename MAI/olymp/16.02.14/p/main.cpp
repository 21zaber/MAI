#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

const long long big_ass_int = 1000*1000*1000;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<vector<short> > k(n, vector<short>(m));

    for (int i = 0 ; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            char chr;
            cin >> chr;
            k[i][j] = chr - '0';
        }
    }

    pair<long long, long long> start = make_pair(0, 0);
    pair<long long, long long> finish = make_pair(n-1, m-1);

    pair<long, long> directions[4] = {make_pair(1, 0), make_pair(-1, 0), make_pair(0, 1), make_pair(0, -1)};
    vector<vector<long long> > dist(n, vector<long long>(m, big_ass_int));
    vector<vector<bool> > inqueue(n, vector<bool>(m, false));
    queue<pair<long long, long long> > q = queue<pair<long long, long long> >();

    dist[start.first][start.second] = 0;
    q.push(start);
    inqueue[start.first][start.second] = true;

    while (!q.empty()) {
        pair<long long, long long> v = q.front();
//cout << "(" << v.first << "," << v.second << ")" << endl;

        for (int i = 0; i < 4; ++i) {
            pair<long long, long long> dir = directions[i];
            long long x = v.first + dir.first * k[v.first][v.second];
            long long y = v.second + dir.second * k[v.first][v.second];
            if (x >= 0 && x < n && y >= 0 && y < m) {
                if (!inqueue[x][y] && dist[x][y] > dist[v.first][v.second] + 1) {
                    dist[x][y] = dist[v.first][v.second] + 1;
                    q.push(make_pair(x, y));
                    inqueue[x][y] = true;
//cout << "      -> (" << x << ", " << y << ")" << endl;

                    if (x == finish.first && y == finish.second) {
                        break;
                    }
                }
            }
        }

        q.pop();
        inqueue[v.first][v.second] = false;
    }

    if (dist[finish.first][finish.second] == big_ass_int) {
        cout << -1 << endl;
    }
    else {
        cout << dist[finish.first][finish.second] << endl;
    }

    return 0;
}
