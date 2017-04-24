n = int(input())

br = []
q = []

for i in range(n):
    x, y = map(int, input().split())
    br.append((x, y))

t = 10 ** 10
tt = 10 ** 9
br.sort(key=lambda x: x[0] * t + x[1] + tt)

from collections import defaultdict as ddict
hs = set()
ls = ddict(list)

lst = None
for i in range(n):
    b = br[i]
    x, y = b
    if lst is None:
        lst = [x, y, 1]
        continue
    xp, yp = br[i-1]
    if x == xp and y == yp + 2:
        lst[-1] += 1
    else:
        x, y, l = lst
        hs.add(x)
        ls[x].append((x, y, l))
        lst = [b[0], b[1], 1]

ls[lst[0]].append(lst)
hs.add(lst[0])

hs = list(hs)
hs.sort()
checked = set()
ans = 0


def check(h):
    global checked, ls, ans

    if h+1 in ls:
        nw = [(l[0]+1, l[1]+1, l[2]-1) for l in ls[h] if l[2] > 1]
        nxt = ls[h+1]
        m = nw + nxt
        m.sort(key=lambda x: x[1])
        nw = []
        for l in m:
            if len(nw) < 1:
                nw.append(l)
                continue
            y, ln = l[1:]
            yp, lp = nw[-1][1:]
            if yp + lp*2 >= y:
                nw[-1] = (h+1, yp, max(lp, (y + 2 * ln - yp) // 2))
            else:
                nw.append(l)
        ls[h+1] = nw

    else:
        for l in ls[h]:
            x, y, ln = l
            if ln > 1:
                ls[h+1].append((x+1, y+1, ln-1))

    for i in ls[h]:
        ans += i[-1]

    if len(ls[h+1]) > 0:
        return h+1
    else:
        return None

for h in hs:
    hh = h
    while hh is not None:
        if hh in checked:
            hh = None
            continue
        else:
            checked.add(hh)
        
        hh = check(hh)

print(ans)
