#!/usr/bin/python3.5

t = int(input())

def zf (s):
    n = len(s)
    z = [0 for i in range(n)]
    i,l,r = 1,0,0
    while i < n:
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        i += 1
    return z

for i in range(t):
    n, m, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    na = []
    for q in range(p):
        na += [a[i] for i in range(q,n,p)] + ['#']

    na = b + ['$'] + na
    z = zf(na)
    print(z.count(len(b)))

