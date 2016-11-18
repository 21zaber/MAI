#!/usr/bin/python3.5
from copy import deepcopy as copy

right = 0
top = 1
left = 2
bot = 3

def r_left(a): # <
    return (a + 1) % 4

def r_right(a):# >
    return (a - 1) % 4

def f_hor(a):# -
    if a % 2 != 0:
        return (a + 2) % 4
    return a

def f_ver(a):# |
    if a % 2 == 0:
        return (a + 2) % 4
    return a

def f_d2(a):# \
    if a % 2 == 0:
        return a + 1
    if a % 2 != 0:
        return a - 1

def f_d1(a):# /
    return 3 - a

coms = {'<': r_left,
        '>': r_right,
        '-': f_hor,
        '|': f_ver,
        '\\':f_d1,
        '/': f_d2}

syms = ['<', '>', '^', 'v', 'o', 'x', '|', '-', '/', '\\']
def_conv = {}
for i in syms:
    def_conv[i] = i

conv = None
x, y = None, None
f = None


def flip_hor():
    global x, y, f, conv
    f = f[::-1]
 
    for k, v in conv.items():
        if v == '>':
            conv[k] = '<'
        elif v == '<':
            conv[k] = '>'
        elif v == '/':
            conv[k] = '\\'
        elif v == '\\':
            conv[k] = '/'
 
    x = coms['-'](x)
    y = coms['-'](y)
 
def rotate_right():
    global x, y, f, conv
    n = len(f)
    new_f = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_f[i][j] = f[n-j-1][i]

    for i in range(n):
        f[i] = ''.join(new_f[i])
 
    for k, v in conv.items():
        if v == '>':
            conv[k] = '^'
        elif v == 'v':
            conv[k] = '>'
        elif v == '<':
            conv[k] = 'v'
        elif v == '^':
            conv[k] = '<'
        elif v == '/':
            conv[k] = '\\'
        elif v == '\\':
            conv[k] = '/'
        elif v == '|':
            conv[k] = '-'
        elif v == '-':
            conv[k] = '|'
 
    x = coms['>'](x)
    y = coms['>'](y)

while True:
    try:
        n = int(input())
    except:
        break

    f = []
    for i in range(n):
        f.append(input())
    
    conv = copy(def_conv)
    
    cmds = input()
    x, y = right, top

    for i in input()[::2]:
        x = coms[i](x)
        y = coms[i](y)

    while x != right:
        rotate_right()

    if y != top:
        flip_hor()


    new_f = ['' for i in range(n)]

    for i in range(len(f)):
        for j in range(len(f)):
            new_f[i] += conv[f[i][j]]

    print('\n'.join(new_f))

    

