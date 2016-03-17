from copy import deepcopy as copy

class Vector(list):
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
    
    def __str__(self):
        return ' '.join(list(map(lambda s: str(s).ljust(4), self)))

    def __abs__(self):
        c = 0
        for i in self:
            c += abs(i)
        return c

    def read(self, s):
        self = list(map(float, s.split()))

v = Vector([1, 2, 3])

print v
print abs(v)
