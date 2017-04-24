n = int(input())

q = n+3

t = [[[[0 for i in range(q)] for i in range(q)] for i in range(q)] for i in range(n+1)]

# len vs max last
t[1][0][0][0] = 1
for l in range(1, n):
    for vs in range(l+1):
        for mx in range(l):
            for lst in range(mx+1):
                c = 0
                if t[l][vs][mx][lst] == 0:
                    continue
                for i in range(vs+2):
                    if i <= lst:
                        t[l+1][vs][mx][i] += t[l][vs][mx][lst]
                        c+=1
                    elif i >= mx:
                        t[l+1][vs+1][i][i] += t[l][vs][mx][lst]
                        c+=1

                #print('l: {}, vs: {}, m: {}, lst: {}, c: {}'.format(l, vs, mx, lst, c))

ans = 0
for i in t[-1]:
    for j in i:
        for k in j:
            ans += k

print(ans)
