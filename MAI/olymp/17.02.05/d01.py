n = int(input())

l = input()

def g(N, L):
    t = []
    n = N
    l = L
    for i in range(L):
        q = n / l
        if q > int(q):
            q = int(q) + 1
        else:
            q = int(q)
        n -= q
        l -= 1
        t.append(q)

    return t

ans = (100, [])

for i in range(1, len(l)+1):
    a = g(n, i) + [0] * (len(l) - i)
    s = 0
    for i in range(5):
        if l[i] == 'Y':
            s += a[i]
    if s < ans[0]:
        ans = (s, a)

print(ans[0])
print(' '.join(map(str, ans[1])))

