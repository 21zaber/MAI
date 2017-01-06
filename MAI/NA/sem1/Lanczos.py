
from Matrix import Matrix
from Vector import Vector

def tqli(A, B):
    n = len(A)
    e = Vector.new(n=n)
    d = Vector.new(n=n)
    
    e[0] = 0
    for i in range(1, n):
        d[i] = A[i][i]
        e[i] = A[i][i-1]

    for l in range(n):
        while m != l:
            for m in range(l, n-1):
                dd = abs(d[m]) + abs(d[m+1])
                if abs(e[m]) == dd:
                    break;
            if m != l:
                g = (d[l+1] - d[l]) / (2 * e[l])
                r = hypot(1, g)
                if g >= 0:
                    g += abs(r)
                else:
                    g -= abs(r)
                g = d[m] - d[l] + e[l] / g
                s = 1; c = 1; p = 0

            

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
    print(a)
    print()
    print(b)
    return T


if __name__ == '__main__':
    n = 3

    a = Matrix.rand(n=n, m=n)

    for i in range(n):
        for j in range(i, n):
            a[j][i] = a[i][j]

    print(a)
    print()
    print(lanczos(a))
