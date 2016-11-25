#!/usr/bin/python3.5

t = int(input())

fib = [1, 2]

while fib[-1] < 10**9:
    fib.append(fib[-1] + fib[-2])

for i in range(t):
    n = int(input())

    j = 0
    while fib[j] <= n:
        j+=1

    print(n - j)
