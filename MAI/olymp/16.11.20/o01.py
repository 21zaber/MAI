#!/usr/bin/python3.5

from math import sqrt

t = []
s = 0

for i in range(3):
    t.append(list(map(int, input().split())))
    s += t[-1][0] * t[-1][1]

if int(sqrt(s)) ** 2 != s:
    print(0)
    exit()

side  = int(sqrt(s))


f = False

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        k = 3 - i - j
        if side in t[i]:
            if side in t[j] and side in t[k]:
                s = sum([sum(i) for i in t])
                if s == side * 4:
                    f = True

            else:
                sside = side * 2 - sum(t[i])
                if sside in t[j] and sside in t[k]:
                    if sum(t[j]+ t[k]) == sside * 2 + side:
                        f = True

if f:
    print(1)
else:
    print(0)
