#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    std::map<int, vector<pair<int, int> > > m;
    for (int i = 0; i < n; ++i) {
        int s, v;
        cin >> s >> v;
        if (m.find(s) == m.end()) {
            m[s] = vector<pair<int, int> >();
        }
        m[s].push_back(make_pair(v, i + 1));
    }

    vector<pair<int, int> > answers = vector<pair<int, int> >();

    for (map<int, vector<pair<int, int> > >::iterator it = m.begin(); it != m.end(); ++it) {
        int color = it->first;
        vector<pair<int, int> > cards = it->second;

        if (cards.size() < 2) {
            cout << -1 << endl;
            return 0;
        }

        int min1 = -1, min2 = -1;
        for (int i = 0; i < cards.size(); ++i) {
            if (min1 == -1 || cards[i].first < cards[min1].first) {
                min2 = min1;
                min1 = i;
            }
            else if (min2 == -1 || cards[i].first < cards[min2].first) {
                min2 = i;
            }
        }

        int ans1 = cards[min1].second;
        int ans2 = cards[min2].second;
        if (ans1 > ans2) {
            int tmp = ans1;
            ans1 = ans2;
            ans2 = tmp;
        }
        answers.push_back(make_pair(ans1, ans2));
    }

    cout << m.size() << endl;
    for (int i = 0; i < answers.size(); ++i) {
        cout << answers[i].first << ' ' << answers[i].second << endl;
    }
}

