from math import sqrt
c = int(input())

a = 1
while a ** 2 - c + 1 < 0:
    a += 1

ans = 0
t = int(sqrt(2 * (10 ** 6))) + 1
while a < t:
    q = a ** 2 - c + 1
    q = sqrt(q)
    if int(q) - q < 0.1 ** 5:
        ans += 2
    a += 1

print(ans)

