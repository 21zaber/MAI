
n = int(input())

t = list(map(int, input().split()))

t.sort()

l, r = 0, t[-1] * 3

def check(s):
    i = 0
    j = len(t) - 1
    c = 0
    while i < j:
        if t[i] + t[j] < s:
            i += 1
            continue
        if t[i] + t[j] > s:
            j -= 1
            continue
        if t[i] + t[j] == s:
            c += 1
            i += 1
            j -= 1
            continue
    return c

m = 0

for i in range(1, 2001):
    cnt = check(i)
    m = max(m, cnt)

print(m)

