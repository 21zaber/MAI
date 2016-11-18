#!/usr/bin/python3.5
t = 0

def topsort():
    used = [True for i in range(n)]
    pos = [0 for i in range(n)]

    def dfs(v):
        global t
        used[v] = False
        for i in children[v]:
            if used[i]:
                dfs(i)
        pos[v] = t
        t += 1

    dfs(0)
    pos = [n - i - 1 for i in pos]
    nds = [0 for i in range(n)]
    for i in range(n):
        nds[pos[i]] = i
    return nds[::-1] 

n = int(input())
children = [[] for i in range(n)]
parent = [0 for i in range(n)]
value = [0 for i in range(n)]



for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    children[a].append(b)
    parent[b] = a

order = topsort()

ans = 0
mans = 0

for v in order:
    if len(children[v]) == 0:
        value[v] = 1
        mans += 1
    value[parent[v]] += value[v]

for v in order:
    ans = max(ans, min(value[v], mans - value[v]))

print(ans)






