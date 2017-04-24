n = int(input())

l = input()

def r(n, l, m, ans):
    if l == '':
        return 0
    if l[0] == 'N':
        t = min(n, m)
        ans.append(t)
        return r(n-t, l[1:], t, ans)

    q = 0
    w = l.split('Y')
    for i in w:
        if i == '':
            q += 1
        else:
            q += len(i)
            break

    print(q)

    t = n / q
    if t > int(t):
        t = int(t) + 1
    else:
        t = int(t)

    t = min(m, t)
    ans.append(t)
    return t + r(n-t, l[1:], t, ans)

ans = []
print(r(n, l, n, ans))

print(' '.join(list(map(str, ans))))

