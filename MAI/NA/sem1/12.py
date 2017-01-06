from Matrix import Matrix
from Vector import Vector
from copy import deepcopy as copy

log_file = open('log12', 'w')
verb = True

def log(s):
    s = str(s)
    if verb:
        print(s)
    log_file.write(s + '\n')

m = Matrix.new(5, 6)
fin = open('input12', 'r')
for i, s in enumerate(fin.readlines()):
    t = list(map(float, s.split()))
    for j, n in enumerate(t):
        m[i][j] = n
log('Input matrix: ')
log(m)
log('\n')
n = 5


p = [0 for i in range(n)]
q = copy(p)
p[0] = -m[0][1] / m[0][0]
q[0] = m[0][-1] / m[0][0]

for i in range(1, n):
    a = m[i][i-1]
    b = m[i][i]
    c = m[i][i+1]
    if i == n - 1:
        c = 0
    d = m[i][-1]
    pp = p[i-1]
    pq = q[i-1]
    p[i] = -c / (b + a * pp)
    q[i] = (d - a * pq) / (b + a * pp)

log("p: " + str(Vector(p)))
log("q: " + str(Vector(q)))

x = [0 for i in range(n)]
x[-1] = q[-1]
for i in range(n-2, -1, -1):
    x[i] = x[i+1] * p[i] + q[i]

log("x: " + str(Vector(x)))

log_file.close()
