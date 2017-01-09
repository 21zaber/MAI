#!/usr/bin/python3.5
n = int(input())

s = 0
for i in range(1, n+1):
    for j in str(i):
        s += int(j)

print(s % 3 == 0 and n % 2 == 0)
