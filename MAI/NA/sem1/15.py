from Matrix import Matrix
from Vector import Vector
from logging import log
from math import sqrt
from copy import deepcopy as copy

l = log('log15')

m = Matrix.new(3, 3)
fin = open('input15', 'r')
for i, s in enumerate(fin.readlines()):
    t = list(map(float, s.split()))
    for j, n in enumerate(t):
        m[i][j] = n
l.fwrite('Input matrix: ')
l.fwrite(m)
l.fwrite('\n')
n = 3

def hh(step, a):
    def sign(a):
        if a >= 0:
            return 1
        else: 
            return -1
    n = len(a)
    v = Matrix.new(n, 1)
    t = 0
    for i in range(step, n):
        t += a[i][0] ** 2
    t = sqrt(t)
    v[step][0] = a[step][0] + sign(a[step][0]) * t
    for i in range(step + 1, n):
        v[i][0] = a[i][0]
   #l.write('v: ')
   #l.write(v.list())
    vt = v.transpose()
    tmp = vt * v
    tmp = tmp[0][0]
    h = Matrix.E(n) - (v * vt) * (2/tmp) 
    return h

def QR(m, n):
    q = Matrix.E(n)
    r = copy(m)

    for i in range(n):
        h = hh(i, r.get_col(i))
        r = h * r
        q = q * h
    return (q, r)

def get_eigenvalues(a):
    n = len(a)
    res = []
    i = 0
    while i < n:
        t = 0
        for j in range(i + 2, n):
            if a[j][i] > 0.001:
                return None
        if a[i][i+1] < 0.001:
            res.append(a[i][i+1])
            i += 1
            continue

        i += 1

a = copy(m)
iter_n = 1
f = True
while f and iter_n < 100:
    q, r = QR(a, n)
    na = r * q
    l.write('{}:'.format(iter_n))
    l.write('a: ')
    l.write(na)
    a = copy(na)
    iter_n += 1


