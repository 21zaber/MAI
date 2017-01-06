#!/usr/bin/python3.5

from collections import Counter

while True:
    try:
        n = int(input())
    except:
        break
    d = Counter()
    m = []
    for i in range(n):
        t = input()
        d.update(list(t))
        #dd = Counter(list(t))
        m.append(t)
 
    ch = None
    rch = None
    #print(d)
    mf = False
    for i in d.keys():
        if d[i] == 1:
            ch = i
        if d[i] == n + 1:
            ch = i
            mf = True
        if d[i] == n-1:
            rch = i        

    f = False
    x, y = None, None
    if mf:
        for i in range(n):
            d = Counter(m[i])
            if d[ch] == 2:
                for j in range(n):
                    if m[i][j] == ch:
                        for k in range(n):
                            if k != i and m[k][j] == ch:
                                x, y = i+1, j+1
                                f = True
                                break
                    if f:
                        break
            if f:
                break
    else:
        for i in range(n):
            for j in range(n):
                if m[i][j] == ch:
                    x, y = i+1, j+1
                    f = True
                    break
            if f:
                break

    print(x, y, rch)
        
