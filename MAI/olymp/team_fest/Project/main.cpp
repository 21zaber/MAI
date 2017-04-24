#include <iostream>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

struct Brick {
    int h;
    int x;

    Brick() {}
    Brick(int h1, int x1) {
        h = h1;
        x = x1;
    }

    Brick Left() {
        return Brick(h, x-2);
    }
    Brick Right() {
        return Brick(h, x+2);
    }
    Brick UpLeft() {
        return Brick(h+1, x-1);
    }
    Brick UpRight() {
        return Brick(h+1, x+1);
    }
};

struct Line {
    int h;
    int left;
    int right;

    Line() {}
    Line(int h1, int left1, int right1) {
        h = h1;
        left = left1;
        right = right1;
    }

    Line NextLine() {
        return Line(h+1, left+1, right-1);
    }

    bool Empty() {
        return left == right;
    }

    bool SingleBrick() {
        return (right - left == 2);
    }

    int BrickCount() {
        return (right - left) / 2;
    }
};

int brick_cmp(const Brick& a, const Brick& b) {
    if (a.h > b.h)
        return 0;
    if (a.h < b.h)
        return 1;
    if (a.x > b.x)
        return 0;
    if (a.x < b.x)
        return 1;
    return 0;
}

map<int, vector<Line> > rows;

vector<Line> get_next_row(vector<Line>& row) {
    vector<Line> next_row;
    for (int i = 0; i < row.size(); ++i) {
        if (!row[i].SingleBrick()) {
            next_row.push_back(row[i].NextLine());
        }
    }
    return next_row;
}

vector<Line> merge_rows(vector<Line>& row1, vector<Line>& row2) {
    if (row1.size() == 0) return row2;
    if (row2.size() == 0) return row1;

    vector<Line> result;
    int i1 = 0, i2 = 0;
    Line nextLine;

    if (row1[0].left < row2[0].left) {
        nextLine = row1[0];
        i1++;
    }
    else {
        nextLine = row2[0];
        i2++;
    }

    while (i1 < row1.size() || i2 < row2.size()) {
        if (i2 == row2.size()) {
            nextLine = row1[i1];
            i1++;
        }
        else if (i1 == row1.size()) {
            nextLine = row2[i2];
            i2++;
        }
        else if (row1[i1].left < row2[i2].left) {
            nextLine = row1[i1];
            i1++;
        }
        else {
            nextLine = row2[i2];
            i2++;
        }

        if (nextLine.left <= result.back().right + 2) {
            if (nextLine.right > result.back().right) {
                result.back().right = nextLine.right;
            }
        }
        else {
            result.push_back(nextLine);
        }
    }

    return result;
}

long long get_total_count(vector<Line>& row) {
    long long total = 0;
    for (int i = 0; i < row.size(); ++i) {
        total += row[i].BrickCount();
    }
    return total;
}

int main() {

    int n;
    cin >> n;

    // -------------------
    // reading bricks
    // -------------------

    vector<Brick> bricks(n);

    for (int i = 0; i < n; ++i) {
        cin >> bricks[i].h >> bricks[i].x;
    }


    sort(bricks.begin(), bricks.end(), brick_cmp);

//    cout << endl;
//    for (int i = 0; i < bricks.size(); ++i) {
//        cout << bricks[i].h << ' ' << bricks[i].x << endl;
//    }

    // ------------------
    // converting bricks into brick lines
    // ------------------

    int brick_i = 0;
    while (brick_i < bricks.size()) {
        int h = bricks[brick_i].h;
        rows[h] = vector<Line>();
        // loop through bricks on the same row
        for (int i = brick_i+1; i < bricks.size() && bricks[i].h == h; ++i) {
            int left = bricks[i].x;
            // loop through bricks in the same line
            while (i+1 < bricks.size() && bricks[i+1].x == bricks[i].x + 2) {
                i++;
            }
            int right = bricks[i].x;
            rows[h].push_back(Line(h, left, right));

            brick_i = i;
        }

        brick_i++;
    }

    //cout << "main part" << endl;

    long long total = 0;
    map<int, vector<Line> >::iterator row_it = rows.begin();
    while (row_it != rows.end()) {
        vector<Line> current_row = row_it->second;
        int h = row_it->first;
        cout << h << endl;
        row_it++;
        total += get_total_count(current_row);

        while (current_row.size() > 0) {
            current_row = get_next_row(current_row);
            h++;
            if (h == row_it->first) {
                current_row = merge_rows(current_row, row_it->second);
                row_it++;
            }
            total += get_total_count(current_row);
        }
    }

    cout << total << endl;

    return 0;
}
