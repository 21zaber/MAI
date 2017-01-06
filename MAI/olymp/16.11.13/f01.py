#!/usr/bin/python3.5

def comp(a, b):
    return a[0] == b[0] or a[1] == b[1]

used = [True for i in range(4)]
pos = [0 for i in range(4)]

def p(n, k = 0):   
   # print(n, k, pos, used)

    if k == n:
        if k == 1:
            return True
        for i in range(n-1):
            if not comp(cards[pos[i]], cards[pos[i+1]]):
                return False
        return True
    for i in range(n):
        if used[i]:
            used[i] = False
            pos[k] = i
            resp = p(n, k+1)
            used[i] = True
            if resp:
                return True
    return False


while True:
    try:
        l = input().split()
    except:
        l = []
    if len(l) < 1:
        break
    n = int(l[0])
    cards = l[1:]
    if p(n):
         print('YES')
    else:
        print('NO')


