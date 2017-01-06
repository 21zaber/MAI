from Matrix import Matrix
from Vector import Vector
from copy import deepcopy as copy

log_file = open('log13', 'w')
verb = True

def log(s):
    s = str(s)
    if verb:
        print(s)
    log_file.write(s + '\n')

m = Matrix.new(4, 5)
fin = open('input13', 'r')
for i, s in enumerate(fin.readlines()):
    t = list(map(float, s.split()))
    for j, n in enumerate(t):
        m[i][j] = n
log('Input matrix: ')
log(m)
log('\n')
n = 4

a = Matrix.new(4, 4)
for i in range(n):
    for j in range(n):
        a[i][j] = -m[i][j] / m[i][i]
    a[i][i] = 0
b = Matrix.new(4, 1)
for i in range(4):
    b[i][0] = m[i][-1] / m[i][i]
x = Matrix.new(4, 1)

log('a: ')
log(a)
log('b: ')
log(b)
log('x: ')
log(x.list())

log('Simple iteration method: ')

iter_n = 1
f = True
while f and iter_n < 10000:
    nx = b + a * x
    log('{}: '.format(iter_n))
    log(nx.list())
    f = abs(nx - x) > (0.1 ** 5)
    x = copy(nx)
    iter_n += 1


log('\nZeidel iteration method: ')
x = Vector.new(4)

iter_n = 1
f = True
while f and iter_n < 10000:
    nx = Vector.new(n)
    for i in range(n):
        nx[i] = b[i][0]
        for j in range(i):
            nx[i] += a[i][j] * nx[j]
        for j in range(i + 1, n):
            nx[i] += a[i][j] * x[j]
    log('{}: '.format(iter_n))
    log(nx)
    f = abs(nx - x) > (0.1 ** 5)
    x = copy(nx)
    iter_n += 1


