from Matrix import Matrix
from Vector import Vector
from copy import deepcopy as copy

def simple_iteration(w, e):
    n = len(w)
    p = [0 for i in range(n)]
    q = copy(p)
    m = copy(w)
    p[0] = -m[0][1] / m[0][0]
    q[0] = m[0][-1] / m[0][0]

    for i in range(1, n):
        a = m[i][i-1]
        b = m[i][i]
        c = 0
        if i == n - 1:
            c = 0
        else:
            c = m[i][i+1]

        d = e[i][-1]
        pp = p[i-1]
        pq = q[i-1]
        p[i] = -c / (b + a * pp)
        q[i] = (d - a * pq) / (b + a * pp)

    x = [0 for i in range(n)]
    x[-1] = q[-1]
    for i in range(n-2, -1, -1):
        x[i] = x[i+1] * p[i] + q[i]

    return x

#x = [-3, -1, 1, 3, 5]
#f = [-4.2490, -1.7854, 1.7854, 4.2490, 6.3734]
x = [0, 1, 2, 3, 4]
f = [0, 1.8415, 2.9093, 3.1411, 3.2432]
n = len(x)
h = [0] + [x[i]-x[i-1] for i in range(1, n)]

print(f[-3])

a = Matrix.new(n-2, n-2)
b = Matrix.new(n-2, 1)
a[0][0] = 2 * (h[1] + h[2]) 
a[0][1] = h[2]
b[0][0] = 3 * ((f[2] - f[1]) / h[2] - (f[1] - f[0]) / h[1])

for i in range(3, n-1):
    a[i-2][i-3] = h[i-1]
    a[i-2][i-2] = 2 * (h[i-1] + h[1])
    a[i-2][i-1] = h[i]
    b[i-2][0] = 3 * ((f[i] - f[i-1]) / h[i] - (f[i-1] - f[i-2]) / h[i-1])

a[-1][-2] = h[-2]
a[-1][-1] = 2 * (h[-1] + h[-2])
b[-1][0] = 3 * ((f[-1] - f[-2]) / h[-1] - (f[-2] - f[-3]) / h[-2])

a[1][1] *= -1
a[2][2] *= -1


print(a)
print()
print(b)
print()

print(simple_iteration(a, b))
