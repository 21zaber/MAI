#!/usr/bin/python3.5

from sys import stdout


n, m = map(int, input().split())

a = [['0']]

cash = {}

def test(a):
    if len(a) * len(a[0]) == 0:
        return 1
    if len(a) > n or len(a[0]) > m:
        return 0
    t = tuple([tuple(i) for i in a])
    if t in cash:
        return cash[t]
    print('Query: {} {}'.format(len(a), len(a[0])))
    for i in a:
        print(''.join(i))

    stdout.flush()
    r =  int(input())
    cash[t] = r
    stdout.flush()
    return r


r = test(a)
if r == 0:
    print("Answer: ")
    for i in range(n):
        print('1' * m)
    exit()

a[0].append('0')

while len(a[0]) <= m:
    r = test(a)
    if a[0][-1] == '0':
        if r == 0:
            a[0][-1] = '1'
        else:
            a[0].append('0')
    else:
        if r == 0:
            del a[0][-1]
            a[0].extend('0')
            break
        else:
            a[0].append('0')

a[0] = a[0][:-1]

#print(a)

while len(a[0]) <= m:
    r = test(a)
    if a[0][0] == '0':
        if r == 0:
            a[0][0] = '1'
        else:
            a[0] = ['0'] + a[0]
    else:
        if r == 0:
            del a[0][0]
            a[0] = ['0'] + a[0]
            break
        else:
            a[0] = ['0'] + a[0]


a[0] = a[0][len(a[0])-m:]

#print(a)
#print(1111111111111111111111221324)

a += [['?' for i in range(m)]]
a[-1][0] = '0'
f = False
r = test(a)
if r == 1:
    f = True
else:
    a[-1][0] = '1'
    r = test(a)
    if r == 1:
        f = True
    else:
        del a[-1]
 

while f and len(a) <= n:
    for i in range(1, m):
        a[-1][i] = '0'
        r = test(a)
        if r == 0:
            a[-1][i] = '1'
    
    if len(a) <= n-1:
        a += [['?' for i in range(m)]]
        a[-1][0] = '0'
        f = False
        r = test(a)
        if r == 1:
            f = True
        else:
            a[-1][0] = '1'
            r = test(a)
            if r == 1:
                f = True
            else:
                del a[-1]
    else:
        f = False
        

#for i in a:
#    print(' '.join(i))
#print(221324)

a = [['?' for i in range(m)]] + a 
a[0][0] = '0'
f = False
r = test(a)
if r == 1:
    f = True
else:
    a[0][0] = '1'
    r = test(a)
    if r == 1:
        f = True
    else:
        del a[0]

while f and len(a) <= n:
    for i in range(m):
        a[0][i] = '0'
        r = test(a)
        if r == 0:
            a[0][i] = '1'
    
    if len(a) <= n-1:
        a = [['?' for i in range(m)]] + a
    else:
        f = False

print("Answer: ")
for i in a:
    print(''.join(i))

stdout.flush()
