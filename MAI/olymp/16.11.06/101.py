from math import sqrt
n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
s = set(l)
if len(l) > 1:
    s.discard(1)

for i in l:
    if i not in s:
        continue
    for k in range(2, int(sqrt(i)+2)):
        if i % k == 0:
            s.discard(k)
            s.discard(i // k)

t = list(s)
t.sort()
print(' '.join(list(map(str, t))))
