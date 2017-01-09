


int right = 0;
int top = 1;
int left = 2;
int bot = 3;

int r_left(int a){
    return (a + 1) % 4;
}

int r_right(int a){
    return (a - 1) % 4;
}

int f_hor(int a){
    if (a % 2 != 0)
        return (a + 2) % 4;
    return a;
}

int f_ver(int a){
    if (a % 2 == 0)
        return (a + 2) % 4;
    return a;
}

int f_d2(int a){
    if (a % 2 == 0)
        return a + 1;
    return a - 1;
}

int f_d1(int a){
    return 3 - a;
}

map<char, char> conv = {{'<', '<'}, {'>', '>'}, {'^', '^'}, {'v', 'v'}, 
    {'o', 'o'}, {'x', 'x'}, {'|'. '|'}, {'-', '-'}, {'/', '/'}, {'\\', '\\'}};
int x, y;
char **f;


