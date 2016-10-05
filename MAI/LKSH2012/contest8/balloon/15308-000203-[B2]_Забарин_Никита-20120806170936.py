import math

Eps = 0.1 ** 6

inp = open('balloon.in', 'r').read().split('\n')
incount = 0
out = open('balloon.out', 'w')

def input ():
    global incount
    incount += 1
    return inp[incount - 1]

def print(t):
    out.write(t)

class Vector ():    
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
        
        
    def length (self):
        return math.sqrt(self.x ** 2 + self.y ** 2)        

    def normalize (self):
        if self.length() == 0:
            return 
        self.x, self.y = self.x / self.length(), self.y / self.length()
        
    def turn (self, s, c):
        x = self.x
        y = self.y        
        self.x, self.y = x * c - y * s, x * s + y * c
        
    def turn_angle (self, a):
        s = sin(a)
        c = cos(a)
        self.turn(s, c)
        
    def turn_sin (self, s):
        c = math.sqrt(1 - s ** 2)
        self.turn(s, c)
        
    def turn_cos (self, c):
        s = math.sqrt(1 - c ** 2)
        self.turn(s, c)    
    
    def __str__ (self):
        return str(self.x) + ' ' + str(self.y)

    def __mul__ (a, b):        
        if type(b) == float or type(b) == int:
            return Vector(a.x * b, a.y * b)
        return a.x * b.y - a.y * b.x

    def __add__ (a, b):
        return Vector(a.x + b.x, a.y + b.y)

    def __xor__ (a, b):
        return a.x * b.x - a.y * b.y
    
    def __eq__ (a, b):
        return Eq(a.x, b.x) and Eq(a.y, b.y)    
    
    def read(self, s): 
        x, y = map(int, s.split())
        return Vector(x, y)
        
    
class Line():
    def __init__ (self, u = Vector(), v = Vector()):
        self.u, self.v = u, v
        self.v.normalize()
        
    def convert(self):
        self.v = self.v + (self.u * -1)
        
    def new (self, a, b, c):
        self.v.x = -b
        self.v.x = a
        self.u.x = (-a * c) / (a ** 2 + b ** 2)
        self.u.y = (-b * c) / (a ** 2 + b ** 2)
        
    def DistPoint (self, p):
        tmpvect = Vector(p.x - self.u.x, p.y - self.u.y)
        return abs((self.v * tmpvect) / self.v.length())
    
    def __mul__ (a, b):
        q = (b.u * b.v - a.u * b.v) / (a.v * b.v)
        return a.u + a.v * q
    
class Cicrle ():
    def __init__ (self, o = Vector(), r = 0):
        self.o = o
        self.r = r
        
    def tangen (self, p):
        v = makevect(p, self.o)
        l = v.length()
        s = self.r / l
        v.turn_sin(s)
        return Line(p, v)
        
    def __and__ (a, b):
        b.r += -a.r
        l = b.tangen(a.o)
        v = l.v
        v.normalize()
        v = v * a.r
        v.x, v.y = -v.y, v.x
        l.u = l.u + v
        return l
    
def makevect(a, b):
    return Vector(b.x - a.x, b.y - a.y)

def check (a, b, c):
    return a < max(b, c) and a > min(b, c)

def checkeq (a, b, c):
    return a <= max(b, c) and a >= min(b, c)

def Eq (a, b):
    return abs(a - b) < Eps


p, h1, s, h2 = map(int, input().split())

c1 = Cicrle(Vector(0, h1), p)
c2 = Cicrle(Vector(0, h2), s)

l = c1 & c2
l2 = Line(Vector(), Vector(1, 0))
p = l * l2
if p.x >= 0:
    print('0')
else:
    print(str(abs(p.x)))

