#!/usr/bin/python3.5

def conv(a):
    return frozenset([int(i) for i in str(a)])

while True:
    try:
        n = int(input())
    except:
        break

    d = {}
    for i in range(n):
        t = input()
        d[conv(t)] = 1

    print(len(d))

