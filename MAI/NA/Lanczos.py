
from Matrix import Matrix
from Vector import Vector

def lanczos(A):
    k = len(A)

    b = Vector.rand(n=k)
    q = [Vector.new(n=k) for i in range(2)]
    q[1] = b / abs(b)

    b = [0]
    a = [0]

    for i in range(1, k+1):
        z = Vector((A * q[i]).transpose()[0])
        a.append(float(Matrix([q[i]]) * z))
        z = z - q[i] * a[i] - q[i-1] * b[i-1]
        b.append(abs(z))
        if b[i] == 0:
            break
        q.append(z / b[i])

    Q = Matrix(q[-k-1:-1]).transpose()
    T = Q.transpose() * A * Q
    print(Q)
    print()
    return T


n = 5

a = Matrix.rand(n=n, m=n)

for i in range(n):
    for j in range(i, n):
        a[j][i] = a[i][j]

print(a)
print()
print(lanczos(a))
