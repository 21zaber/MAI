
def check(l):
    global a, w
    q = 0
    for i in range((len(a) + l - 1) // l):
        t = 1
        for j in range(l):
            idx = i * l + j
            if len(a) > idx:
                t = max(t, a[idx] + 1)
     #   print('check for', i, t)
        q += t
    return q < w

n, w = map(int, input().split())
a = list(map(int, input().split()))

l, r = 1, n

while l < r:
    m = (l + r) // 2
    #print(l, r, m)
    if check(m):
        r = m - 1
    else:
        l = m

print(l)



        
