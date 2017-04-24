#include <string>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

char swp(char a) {
    if (a == 'A') 
        return 'B'; 
    else 
        return 'A';
}

void ans(char a) {
    if (a == 'A')
        cout << "Bananenfrau" << endl;
    else
        cout << "Apfelmann" << endl;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string s;
        map<char, int> c;
        cin >> s;
        c['A'] = count(s.begin(), s.end(), 'A');
        c['B'] = count(s.begin(), s.end(), 'B');
        int j = 0;
        int sl = s.length();
        for (j = 0; j < sl && s[j] != 'C'; ++j);
        int lp = j-1, rp = j+1;
        if (s[0] == s[s.length()]) {
            ans(s[0]);
            continue;
        }
        char player = 'A';
        //int qwe = 10;
        while (true) {
            //if (qwe < 0) break;
            //qwe--;
            //cout << lp << ' ' << rp << ' ' << player << endl;
            if (lp >= 0 and rp < sl and s[lp] == s[rp] and s[rp] == player) {
                if (s[0] == player) {
                    lp--;
                } else {
                    rp++;
                }
                c[player]--;
            } else if (lp >= 0 and s[lp] == player) {
                lp--;
                c[player]--;
            } else if (rp < sl and s[rp] == player) {
                rp++;
                c[player]--;
            }
            if (c[player] <= 0) {
                ans(swp(player));
                break;
            }
            player = swp(player);
        }
    }
}
