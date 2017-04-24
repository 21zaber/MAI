n = int(input())

l = {}

for i in range(1, n+1):
    t = input()
    l[t] = i

ans = 0

q = set()

#print(l)

nl = [input() for i in range(n)]
nl = nl[::-1]

for i in range(n):
    t = nl[i]
    pos = n - i
    #print("{}: {}".format(t, pos))
    for j in q:
        if l[j] < l[t]:
            #print(j, t)
            ans += 1
            break

    q.add(t)

print(ans)


