#include <iostream>
#include <string>

using namespace std;

string getcoord(int n, int x, int y){
    char ans = '0';
    int t = 1 << (n-1);
    if (y <= t)
        ans = '0';
    else if (y > t * 3)
        ans = '2';
    else if (x <= t)
        ans = '1';
    else        
        ans = '3';

    if (n == 1)
        return string(ans);
    else {
        if (ans == '0')
            return string(ans) + getcoord(n-1, t + 1 - y, x);
        if (ans == '1')
            return string(ans) + getcoord(n-1, x, y - t);
        if (ans == '2')
            return string(ans) + getcoord(n-1, t + 1 - (y - 3*t), x);
        if (ans == '3')
            return string(ans) + getcoord(n-1, x - t, y - t);
    }
}

int main {
    int n,x,y;
    cin >> n >> x >> y;

    string ans = "";
    string lstc = getcoord(n, x, y);

    string steps;
    cin >> steps;

    for (int i = 0; i < steps.size(); ++i){
        char c = steps[i];
        int nx = x, ny = y;
        if (c == "U")
            nx -= 1;
        if (c == "D")
            nx += 1;
        if (c == "R")
            ny += 1;
        if (c == "L")
            ny -= 1;

        string newc = getcoord(n, nx, ny);
        if (newc == lstc)
            ans += 'N'
        else:
            ans += 'Y'
        x = nx;
        y = ny;
        lstc = newc;
    }

    cout << ans;
}
