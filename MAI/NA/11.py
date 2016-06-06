from Matrix import Matrix
from Vector import Vector
from copy import deepcopy as copy

log_file = open('log11', 'w')
verb = True

def log(s):
    s = str(s)
    if verb:
        print(s)
    log_file.write(s + '\n')

m = Matrix.new(4, 5)
fin = open('input11', 'r')
for i, s in enumerate(fin.readlines()):
    t = list(map(float, s.split()))
    for j, n in enumerate(t):
        m[i][j] = n
log('Input matrix: ')
log(m)
log('\n')
n = 4

a = Matrix.new(n, n)
for i in range(n):
    for j in range(n):
        a[i][j] = m[i][j]

u = copy(a)
l = Matrix.new(n, n)

for i in range(n):
    for j in range(i, n):
        l[j][i] = u[j][i] / u[i][i]

for k in range(1, n):
    for i in range(k-1, n):
        for j in range(i, n):
            l[j][i] = u[j][i] / u[i][i]

    for i in range(k, n):
        for j in range(k-1, n):
            u[i][j] = u[i][j] - l[i][k-1] * u[k-1][j]
    print(l)
    print()
    print(u)
    print()

lu = Matrix.new(n, n)
for i in range(n):
    for j in range(n):
        if i < j:
            lu[i][j] = u[i][j]
        else:
            lu[i][j] = l[i][j]

x = [0 for i in range(n)]

for i in range(n):
    b = m[i][-1]
    for j in range(i):
        b -= l[i][j] * x[j]
    x[i] = b

det = 1 
for i in range(n):
    det *= u[i][i]

ra = Matrix.new(n, n)

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if i == j:
            t = 0
            for p in range(j+1, n):
                t += lu[j][p] * ra[p][j]
            ra[j][j] = (1 - t) / lu[j][j]
        if i < j:
            t = 0
            for p in range(i+1, n):
                t += lu[i][p] * ra[p][j]
            ra[i][j] = -t / lu[i][i]
        if i > j:
            t = 0
            for p in range(j+1, n):
                t += lu[p][j] * ra[i][p]
            ra[i][j] = -t
            pass


print('lu: ')
print(lu)
print('l: ')
print(l)
print('u: ')
print(u)
print('x:')
print(x)
print('det:', det)
print('reverse:')
print(ra)
