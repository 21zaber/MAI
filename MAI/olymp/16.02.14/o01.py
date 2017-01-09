n = int(input())

d = {}

for i in range(n):
    s, v = map(int, input().split())
    if s in d.keys():
        d[s].append([v, i + 1])
    else:
        d[s] = [[v, i + 1]]

ans = []

MAX_INT = 10 ** 10

for k in d.keys():
    t = d[k]
    if len(t) < 2:
        print("-1")
        exit()

    m = MAX_INT
    id = -1
    for i in range(len(t)):
        if t[i][0] <= m:
            m = t[i][0]
            id = t[i][1]
    ans1 = id

    m = MAX_INT
    id = -1
    for i in range(len(t)):
        if t[i][0] <= m and t[i][1] != ans1:
            m = t[i][0]
            id = t[i][1]

    if id < ans1:
        ans.append([id, ans1])
    else:
        ans.append([ans1, id])

print(len(ans))
for i in ans:
    print(i[0], i[1])
