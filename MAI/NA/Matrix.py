from copy import deepcopy as copy
from Vector import Vector

class Matrix(Vector):
    #def __init__(self, m = Vector([Vector([1])])):
    #    self.check_matrix()

    def check_matrix(self):
        if len(self) == 0:
            return
        n = len(self[0])
        for i in self:
            if len(i) != n:
                raise TypeError

    def set_size(self, n = 1, m = 1):
        self = Matrix([Vector([0 for i in range(m)]) for i in range(n)])
        for i in range(len(self)):
            for j in range(len(self[i])):
                a[i][j] = self[i][j]
        print "a: ", a
        self = a

    def __str__(self):
        s = ''
        for i in self:
            s += str(i)
        return s[:-1]

    def get_column(self, n):
        return [self[i][n] for i in range(self.n)]

    def __mul__(a, b):
        if type(b) == int or type(b) == float:
            c = copy(a)
            for i in range(a.n):
                for j in range(a.m):
                    c[i][j] *= b
            return c
        if type(b) == Matrix:
            if a.m != b.n:
                raise TypeError
            c = Matrix().set_size(a.n, b.m)
            for i in range(c.n):
                for j in range(c.m):
                    c[i][j] = 0
                    for k in range(a.m):
                        c[i][j] += a[i][k] * b[k][j]
            return c
        raise TypeError    

t = Matrix([Vector([1])])
m = t
print m[0][0]
m.set_size(2, 3)
print m
