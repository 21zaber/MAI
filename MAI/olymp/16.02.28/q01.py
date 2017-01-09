
n = int(input())

for i in range(n):
    c, j = map(int, input().split())
    j += 1
    s = input()
    d = [10**9 for j in range(len(s))]
    d[0] = 0
    for g in range(1, c):
        if s[g] == 'A':
            continue
        for k in range(max(0, g-j), g):
            if s[k] == 'A':
                continue
            d[g] = min(d[g], d[k] + 1)

    if d[-1] != 10**9:
        print(d[-1])
    else:
        print(-1)




