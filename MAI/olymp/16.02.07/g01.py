l, r = map(int, input().split())

def getlog(a):
    return len(str(a))

def geti(a, i):
    if i > getlog(a):
        return 0
    return int(list("000000000000000000000" + str(a))[-i-1])

def mul(a):
    t = list(map(int, list(str(a))))
    a = 1
    for i in t:
        a *= i
    return a

ans = r

powers = [10 ** i for i in range(25)]

finish = getlog(r)

for i in range(finish + 1):
    dig = geti(ans, i)
    if dig != 9:
        t = ans - (dig + 1) * powers[i]
        if t < 0:
            continue
        for j in range(i):
            t += (9 - geti(t, j)) * powers[j] 
    else:
        continue
    if t < l:
        break
    if mul(t) > mul(ans):
        ans = t

print(ans)

    
