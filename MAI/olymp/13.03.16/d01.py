l, n, k = map(int, input().split())


for i in range(l):
    s = (n // k) * 2 - 1
    if n % k > 2:
        n -= 2
    else:
        n -= n % k
    n -= s

if n > 0:
    print(n)
else:
    print(0)
