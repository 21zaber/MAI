import sys

inf = -1

def test(a):
    #if mas[a-1] != inf:
    #    return mas[a-1]
    print('?', a)
    sys.stdout.flush()
    return int(input())
    #mas[a-1] = int(input())
    #return mas[a-1]

def check(a):
    ta = test(a) 
    if a == 1:
        tb = test(a + 1)
        if tb == ta:
            return [a, a + 1]
        print('!', test(a))
        exit()
    tb = test(a-1)
    if ta == tb:
        return [a-1, a]
    if a == n:
        print('!', test(n))
        exit()
    tc = test(a+1)
    if ta == tc:
        return [a, a+1]
    print('!', ta)
    exit()

l, r = 1, int(input()) + 1

n = r - 1

mas = [inf for i in range(r-1)]

while r - l > 1:
    m = (l + r) // 2
    t = check(m)
    if t[0] % 2 == 1:
        l = m
    else:
        r = m

print('!', test(l))

