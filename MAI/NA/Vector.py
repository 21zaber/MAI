from copy import deepcopy
from math import sqrt

def f2s(a):
    MAX_LEN = 7

    if isinstance(a, int):
        return str(a).rjust(MAX_LEN+1, ' ')

    a = round(a, 3)
    if abs(a) < 0.001:
        a = 0.0

    if a >= 0:
        return ' ' + str(a).ljust(MAX_LEN, '0')[:MAX_LEN]
    else:
        return str(a).ljust(MAX_LEN+1, '0')[:MAX_LEN+1]

class Vector(list):

    @staticmethod
    def new(n = 1):
        return Vector([0.0 for i in range(n)])

    @staticmethod
    def E(n = 1):
        return Vector([1.0 for i in range(n)])

    def __mul__(a, b):
        if isinstance(b, (int, float)):
            return Vector([i * b for i in a])
        if isinstance(b, Vector):
            if len(a) != len(b):
                raise Exception("Different vector leght {} and {}".format(a, b))
            return sum([a[i] * b[i] for i in range(len(a))])

        raise Exceptoin("Wrong argument type {}".format(type(b)))

    def __rmul__(a, b):
        if isinstance(b, (int, float)):
            return Vector([i * b for i in a])

        raise Exceptoin("Wrong argument type {}".format(type(b)))

    def __truediv__(a, b):
        if isinstance(b, (int, float)):
            return Vector([i / b for i in a])

        raise Exceptoin("Wrong argument type {}".format(type(b)))

    def __xor__(a, b):
        if isinstance(b, Vector):
            if len(a) != len(b):
                raise Exception("Different vector leght {} and {}".format(a, b))
            return sum([a[i] * b[i] for i in range(len(a))])

        raise Exceptoin("Wrong argument type {}".format(type(b)))

    def __add__(a, b):
        if isinstance(b, Vector):
            if len(a) != len(b):
                raise Exception("Different vector leght {} and {}".format(a, b))
            return Vector([a[i] + b[i] for i in range(len(a))])

        raise Exception("Wrong argument type {}".format(type(b)))

    def __iadd__(a, b):
        return a + b

    def norm(self):
        t = sqrt(sum([i ** 2 for i in self]))
        return self / t

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
        self = Vector(map(float, s.split()))

    def __copy__(self):
        return deepcopy(self)

def test():
    a = Vector([1, 2, 3])
    b = a
    a *= 2
    b = 5 * b
    print(a, b, sep='\n')
    print(a * b)
    print(a + b)
    print(a - b)
    print(abs(a))
    print(a.norm())

if __name__ == "__main__":
    test()


