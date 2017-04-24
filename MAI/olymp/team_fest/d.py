n = int(input())

br = []
q = []

for i in range(n):
    x, y = map(int, input().split())

    br.add((x, y))
    q.append((x, y))


i = 0
while i < len(q):
    b = q[i]

    if (b[0], b[1] + 2) in br:
        br.add((b[0]+1, b[1]+1))
        q.append((b[0]+1, b[1]+1))

    if (b[0], b[1] - 2) in br:
        br.add((b[0]+1, b[1]-1))
        q.append((b[0]+1, b[1]-1))

    i += 1


print(len(br))


