n = int(input())

def check(a):
    v = 0
    m = 0
    for i in range(len(a) - 1):
        if a[i] < a[i+1] and a[i+1] < m:
            return False
        m = max(m, a[i])
        #print(m, v, a[i])
        if a[i] > v+1:
            return False
        if i > 0 and a[i] > a[i-1]:
            v += 1

    if a[-1] > v+1:
        return False

    return True

ans = 0

def r(m):
    global ans
    if len(m) == n:
        if check(m):
            ans += 1
            #print(m)
            return
        else:
            return
    for i in range(len(m)+1):
        r(m + [i])

#print(check([0,1,2]))
r([])
print(ans)


    
