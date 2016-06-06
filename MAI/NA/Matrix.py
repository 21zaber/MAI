from copy import deepcopy as copy
from Vector import Vector

class Matrix(Vector):
    @staticmethod
    def new(n = 1, m = 1):
        v = Vector.new(m)
        return Matrix([copy(v) for i in range(n)])

    @staticmethod
    def E(n = 1):
        m = Matrix.new(n, n)
        for i in range(n):
            m[i][i] = 1
        return m
    
    def __str__(self):
        s = ''
        for i in self:
            s += str(i) + '\n'
        return s[:-1] 

    def get_col(self, n):
        m = Matrix.new(len(self), 1)
        for i in range(len(self)):
            m[i][0] = self[i][n]
        return m
    def get_row(self, n):
        return self[n]
    def swap_col(self, a, b):
        for i in range(len(self)):
            self[i][a], self[i][b] = self[i][b], self[i][a]
    def swap_row(self, a, b):
        self[a], self[b] = self[b], self[a]
    
    def transpose(self):
        m = Matrix.new(len(self[0]), len(self))
        for i in range(len(self)):
            for j in range(len(self[0])):
                m[j][i] = self[i][j]
        return m

    def list(self):
        if len(self) != 1 and len(self[0]) != 1:
            raise TypeError
        if len(self) == 1:
            return self[0]
        else:
            return Vector([self[i][0] for i in range(len(self))])

    def __mul__(a, b):
        if type(b) == int or type(b) == float:
            c = copy(a)
            for i in range(len(a)):
                for j in range(len(a[0])):
                    c[i][j] *= b
            return c
        if type(b) == Matrix:
            if len(a[0]) != len(b):
                raise TypeError
            c = Matrix.new(len(a), len(b[0]))
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] = 0
                    for k in range(len(a[0])):
                        c[i][j] += a[i][k] * b[k][j]
            return c
        raise TypeError 
    def __add__(a, b):
        if type(b) != type(a):
            raise TypeError
        if len(a) != len(b):
            raise TypeError
        if len(a) == 0:
            return copy(a)
        if len(a[0]) != len(b[0]):
            raise TypeError
        if len(a[0]) == 0:
            return copy(a)
        c = Matrix.new(len(a), len(a[0]))
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[i][j] = a[i][j] + b[i][j]
        return c

    def __sub__(a, b):
        return a + (b * -1)
