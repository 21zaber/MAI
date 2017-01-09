#include <iostream>
#include <stdio.h>
#include "stdlib.h"
#include <string.h>

using namespace std;

typedef struct node_s {
    int value;
    int size;
    int x, y;
    struct node_s *left, *right, *par;
} node_t;

void outtree(node_t *t) {
    if (!t) return;
    cout << t->value << endl;
    //if (t->left) cout << "left\n";
    outtree(t->left);
    //if (t->right) cout << "right\n";
    outtree(t->right);
}

node_t *get(int v) {
    node_t *n = (node_t *)calloc(1, sizeof(*n));
    n->value = v;
    //cout << v << " new\n";
    return n;
}

int size(int a) {
    int ans = 1;
    while (a > 9) {
        ++ans;
        a /= 10;
    }
    return ans;
}

int calcsize(node_t *tree) {
    if (!tree) return 0;

    tree->size = size(tree->value) + calcsize(tree->left) + calcsize(tree->right);
    return tree->size;
}

int height(node_t *t) {
    if (!t) return 0;
    int l = height(t->left)  + 1;
    int r = height(t->right) + 1;
    return l > r ? l : r;
}

void draw(node_t *t, char *s) {
    if (!t) return;
    //cout << t->value << ' ' << t->x << ' ' << t->y << endl;
    int x = t->value;
    for (int i = size(t->value) - 1; i >= 0; --i) {
        //cout << i << endl;
        s[t->y + i] = x % 10 + 1;
        //cout << i << endl;
        x /= 10;
        //cout << i << endl;
    }
}

bool isleft(node_t *t) {
    if (!t or !t->par) return true;
    if (!t->par->left) return false;
    return t->par->left->value == t->value;
}

void drawnode(node_t *t, char *s, int lvl) {
    if (!t) return;
    if (!t->par) {
        t->x = 0;
        t->y = t->left ? t->left->size : 0;
    } else {
        if (isleft(t)) {
            t->x = t->par->x + 1;
            t->y = t->par->y - size(t->value) - (t->right ? t->right->size : 0);
        } else {
            t->x = t->par->x + 1;
            t->y = t->par->y + size(t->par->value) + (t->left ? t->left->size : 0);
        }
    }
    if (lvl == 0) {
        draw(t, s);
        return;
    }
    drawnode(t->left, s, lvl - 1);
    drawnode(t->right, s, lvl - 1);
}

void printtree(node_t *t) {
    int h = height(t);
    calcsize(t);
    char *s = (char *)calloc(t->size, sizeof(char));
    for (int i = 0; i < h; ++i) {
        drawnode(t, s, i);
        int n = t->size;
        for (int j = t->size - 1; j >= 0; --j, --n) {
            if (s[j] != 0) break;       
        }    
        for (int j = 0; j < n; ++j) {
            if (s[j] == 0) {
                cout << ' ';
            } else {
                cout << s[j] - 1;
            }    
        }
        cout << endl;
        memset(s, 0, sizeof(char) * t->size);
    }
}

int main() {
    node_t *cur = NULL, *tree = NULL;
    int prev;
    while(!cin.eof()) {
        int a;
        cin >> a;
        if (a == prev) break;
        prev = a;
        //cout << a << " qwerwer\n";
        if (!cur) {
            cur = get(a);
            continue;
        }
        if (a < cur->value) {
            node_t *n = get(a);
            n->par = cur;
            cur->left = n;
            cur = n;
            continue;
        }
        while (cur->par and a > cur->par->value) {
            cur = cur->par;
        }
        if (!cur->right) {
            node_t *n = get(a);
            n->par = cur;
            cur->right = n;
            cur = n;
            continue;
        }
        cur = cur->right;
        while (cur->value != a) {
            if (cur->value < a) {
                if (!cur->right) {
                    node_t *n = get(a);
                    n->par = cur;
                    cur->right = n;
                    cur = n;
                    continue;
                }
                cur = cur->right;
            } else {
                if (!cur->left) {
                    node_t *n = get(a);
                    n->par = cur;
                    cur->left = n;
                    cur = n;
                    continue;
                }
                cur = cur->left;
            }
        }
    }
    while (cur->par) {
        cur = cur->par;
    }
  //outtree(cur);
  //cout << "test\n";
  //cout << calcsize(cur) << endl;
  //cout << "test\n";
  //cout << height(cur) << endl;
  //cout << "test\n";
    printtree(cur);
}
