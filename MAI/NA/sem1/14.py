from Matrix import Matrix
from Vector import Vector
from logging import log
from copy import deepcopy as copy

l = log('log14', False)

m = Matrix.new(3, 3)
fin = open('input14', 'r')
for i, s in enumerate(fin.readlines()):
    t = list(map(float, s.split()))
    for j, n in enumerate(t):
        m[i][j] = n
l.fwrite('Input matrix: ')
l.fwrite(m)
l.fwrite('\n')
n = 3

from math import cos, sin, atan, pi

def get_rotate_matrix(n, i, j, angle):
    m = Matrix.new(n, n)
    for k in range(n):
        if k not in [i, j]:
            m[k][k] = 1
    s = sin(angle)
    c = cos(angle)
    m[i][j] = -s
    m[j][i] = s
    m[i][i] = c
    m[j][j] = c
    return m

u = Matrix.new(n, n)
for i in range(n):
    u[i][i] = 1

iter_n = 1
f = True
while f and iter_n < 1000:
    q = 0
    qi, qj = 0, 0
    for i in range(n):
        for j in range(n):
            if i != j and abs(m[i][j]) > q:
                q, qi, qj = abs(m[i][j]), i, j
    angle = pi / 4
    if abs(m[qi][qi] - m[qj][qj]) > 0.000001:
        angle = atan(2 * m[qi][qj] / (m[qi][qi] - m[qj][qj])) / 2
    
    rm = get_rotate_matrix(n, qi, qj, angle)
    rmt = rm.transpose()
    nm = rmt * m * rm

    u = u * rm 

    l.write('{}: '.format(iter_n))
    l.write(nm)
    s = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                s += nm[i][j] ** 2

    f = abs(s) > (0.1 ** 5)
    m = copy(nm)
    iter_n += 1

l.fwrite("Eigenvalues: ")
values = Vector([m[i][i] for i in range(n)])
l.fwrite(values)
l.fwrite("Eigenvectors: ")
l.fwrite(u.transpose())

