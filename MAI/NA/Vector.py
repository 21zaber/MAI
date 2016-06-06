from copy import deepcopy as copy

def f2s(a):
    #return str(a)
    a = round(a, 3)
    if a <= 0 and abs(a) < 0.001:
        a = abs(a)
    if a >= 0:
        return ' ' + str(a).ljust(5, '0')[:5]
    else:
        return str(a).ljust(6, '0')[:6]

class Vector(list):
    @staticmethod
    def new(n = 1):
        return Vector([0 for i in range(n)])
    def __mul__(a, b):
        if type(b) == int or type(b) == float:
            c = copy(a)
            for i in range(len(c)):
                c[i] *= b
            return c

        raise TypeError

    def __add__(a, b):
        if type(b) == Vector:
            c = copy(a)
            for i in range(len(c)):
                c[i] += b[i]
            return c
        raise TypeError

    def __sub__(a, b):
        if type(b) != type(a):
            raise TypeError
        return a + (b * -1)
    
    def __str__(self):
        return ' '.join(list(map(f2s, self)))

    def __abs__(self):
        c = 0
        for i in self:
            a = abs(i)
            if a > c:
                c = a
        return c

    def read(self, s):
        self = list(map(float, s.split()))
