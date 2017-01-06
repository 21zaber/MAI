import sys

def test(a):
    if a <= 0:
        return 0
    print('?', a)
    sys.stdout.flush()
    return int(input())

def check(a):
    ta = test(a)
    tl = test(a - 1)
    if ta == tl:
        return True
    return False

l, r = -4, int(input()) + 1 

while r - l > 2:
    #print('\t', l, r)
    m = (l + r) // 2
    m -= m % 2
    if check(m):
        l = m
    else:
        r = m
    #print('\t', l, r)

print('!', test(l + 1))
