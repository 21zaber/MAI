n = int(input())

from collections import defaultdict
from math import sqrt
v = defaultdict(float)

for i in range(n):
    a, b, c, d = map(int, input().split())
    vect = (abs(c-a), abs(d-b),)
    if vect == (0,0,):
        continue
    l = sqrt(vect[0] ** 2 + vect[1] ** 2)
    vect = tuple([i/l for i in vect])
    v[vect] += 0.5


t = []
for i in v:
    t.append(v[i])

t.sort()

t = [int(i) for i in t]

ans = 0
tmp = 0

for i in t:
    ans += min(tmp, i)
    tmp = max(i, tmp) - min(i, tmp)

print(ans)

