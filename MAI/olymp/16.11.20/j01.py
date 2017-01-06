#!/usr/bin/python2.7

from math import sqrt, pi

n, s = map(int, raw_input().split())

v = []

for i in range(n):
    x, y = map(int, raw_input().split())
    v.append([x, y])

ms = 0.0
p = 0.0

for i in range(n):
    ms += (v[i][0] - v[i-1][0]) * (v[i][1] + v[i-1][1]) / 2
    p += sqrt((v[i][0] - v[i-1][0]) ** 2 + (v[i][1] - v[i-1][1]) ** 2)

ms = abs(ms)

#print(ms)
#print(p)

if ms >= s:
    print(0.0)
    exit()

a = pi
b = p
c = ms - s

d = b ** 2 - 4 * a * c
sd = sqrt(d)

x1 = (-b + sd) / 2 / a
x2 = (-b - sd) / 2 / a

#print(x1, x2)

ans = [x1, x2]
ans = [i for i in ans if i > 0]

print min(ans)

