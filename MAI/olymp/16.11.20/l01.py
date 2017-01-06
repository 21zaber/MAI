#!/usr/bin/python3.5

def add(p, q, a, b):
    return (b*q, a*q + p)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

t = int(input())
for e in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    p, q = b[-1], a[-1]
    #print('{}/{}'.format(p, q))
    for i in range(n-2, -1, -1):
        #print(i)
        #print('p : {}, q: {}, a: {}, b {}'.format(p, q, a[i], b[i]))
        p, q = add(p, q, a[i], b[i])

    t = gcd(p, q)
    p //= t
    q //= t

    print('{}/{}'.format(p, q))

