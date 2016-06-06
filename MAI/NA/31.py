from math import atan

class Function():
    def __init__(self, f, x):
        self.f = f
        self.x = x
        self.y = [f(i) for i in x]
        self.n = len(x)

    def dif(self, x):
        if len(x) == 1:
            return self.y[x[0]]
        return (self.dif(x[:-1]) - self.dif(x[1:])) / (self.x[x[0]] - self.x[x[-1]])

    def orig(self, x):
        return self.f(x)

    def getmax(self):
        m = 0
        st = self.x[0]
        fn = self.x[-1]
        step = (fn - st) / 1000
        x = st
        while x <= fn:
            t = abs(self.f(x))
            m = max(t, m)
            x += step
        return m

    def newton(self, x):
        t = [i for i in range(self.n)]
        f = 0
        for i in range(self.n):
            l = 1
            for j in range(i):
                l *= (x - self.x[j])
            f += l * self.dif(t[:i+1])
        return f

    def lagrange(self, x):
        n = self.n
        f = 0
        for i in range(n):
            l = 1
            for j in range(n):
                if i != j:
                    l *= (x - self.x[j]) / (self.x[i] - self.x[j])
            f += l * self.y[i]
        return f

    def getprec(self, x):
        prec = self.getmax()
        for i in range(self.n):
            prec *= (x - self.x[i]) / (i + 1)
        return abs(prec)

        

f1 = Function(lambda x:atan(x) + x, [-3, -1, 1, 3])
f2 = Function(lambda x:atan(x) + x, [-3, -2, 1, 3])
x = -0.5

print('f(x)          =', f1.orig(x))
print('a)newton(x)   =', f1.newton(x))
print('a)lagrange(x) =', f1.lagrange(x))
print('a)precision     ', f1.getprec(x))
print('b)newton(x)   =', f2.newton(x))
print('b)lagrange(x) =', f2.lagrange(x))
print('b)precision     ', f2.getprec(x))
