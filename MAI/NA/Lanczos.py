
from Matrix import Matrix
from Vector import Vector
from math import sqrt

def QRalg(m):
    from copy import deepcopy as copy
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

    m = copy(m)
    n = len(m)

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

       #l.write('{}: '.format(iter_n))
       #l.write(nm)
        s = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    s += nm[i][j] ** 2

        f = abs(s) > (0.1 ** 5)
        m = copy(nm)
        iter_n += 1

    values = Vector([m[i][i] for i in range(n)])
    vectors = u.transpose()
    for i in range(len(vectors)):
        if abs(vectors[i][-1]) > 0.001:
            vectors[i] *= 1/vectors[i][-1]
    return (values, vectors, )

def lanczos(A):
    k = len(A)

    b = Vector.rand(n=k)
    q = [Vector.new(n=k) for i in range(2)]
    q[1] = b / abs(b)

    b = [0]
    a = [0]

    for i in range(1, int(2 * sqrt(k))):
        z = Vector((A * q[i]).transpose()[0])
        a.append(float(Matrix([q[i]]) * z))
        z = z - q[i] * a[i] - q[i-1] * b[i-1]
        for j in q:
            z -= j * (z * j)
        for j in q:
            z -= j * (z * j)
        b.append(abs(z))
        if b[i] == 0:
            break
        q.append(z / b[i])

    Q = Matrix(q[-k-1:-1]).transpose()
    T = Q.transpose() * A * Q
    print(Q)
    print()
    return (Q, T, )

def wprint(m):
    print('{', end='')
    for i in m:
        print('{', end='')
        print(*i, sep=', ', end = '')
        print('}', end=', ')
    print('}', end='')
        

n = 16

a = Matrix.rand(n=n, m=n)

for i in range(n):
    for j in range(i, n):
        a[j][i] = a[i][j]

print(a)
wprint(a)
print()
Q, T = lanczos(a)
values, vectors = QRalg(T)
vectors *= Q.transpose()# * vectors
for i in range(len(vectors)):
    if abs(vectors[i][-1]) > 0.001:
        vectors[i] *= 1/vectors[i][-1]

print(T)

t = [(values[i], vectors[i], ) for i in range(len(values))]
t.sort(key=lambda x: abs(x[0]), reverse=True)

print()
print(Vector([i[0] for i in t]))
print()
print(Matrix([i[1] for i in t]))

values, vectors = QRalg(a)
t = [(values[i], vectors[i], ) for i in range(len(values))]
t.sort(key=lambda x: abs(x[0]), reverse=True)

print()
print(Vector([i[0] for i in t]))
print()
print(Matrix([i[1] for i in t]))
