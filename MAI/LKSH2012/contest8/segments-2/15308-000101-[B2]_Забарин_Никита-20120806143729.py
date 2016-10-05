import math

Eps = 0.1 ** 6

inp = open('segments.in', 'r').read().split('\n')
incount = 0
out = open('segments.out', 'w')

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
    
def makevect(a, b):
    return Vector(b.x - a.x, b.y - a.y)

def check (a, b, c):
    return a < max(b, c) and a > min(b, c)

def checkeq (a, b, c):
    return a <= max(b, c) and a >= min(b, c)

def Eq (a, b):
    return abs(a - b) < Eps
       
a, b, c, d = Vector(), Vector(), Vector(), Vector()       
a = a.read(input())     
b = b.read(input())
c = c.read(input())
d = d.read(input())

if a.x > b.x or (a.x == b.x and a.y > b.y):
    a, b = b, a
    
if c.x > d.x or (c.x == d.x and c.y > d.y):
    c, d = d, c

ab = makevect(a, b)
ad = makevect(a, d)
ac = makevect(a, c)
dc = makevect(d, c)
da = makevect(d, a)
db = makevect(d, b)

if a == b:
    if makevect(c, a) * makevect(c, d) == 0:
        if checkeq(a.x, c.x, d.x):
            print(str(a))
            exit()
        if a.x == c.x and checkeq(a.y, c.y, d.y):
            print(str(a))
            exit()            
    print('Empty')
    exit() 
 
if d == c:
    if makevect(a, c) * makevect(a, b) == 0:
        if checkeq(c.x, a.x, b.x):
            print(str(c))
            exit()
        if a.x == c.x and checkeq(c.y, a.y, b.y):
            print(str(c))
            exit()         
    print('Empty')
    exit()   

if ((ab * ad) * (ab * ac) > 0) or ((dc * da) * (dc * db) > 0):
    print('Empty')
    exit()
    
l1 = Line(a, ab)
l2 = Line(c, makevect(c, d))

if l1.v == l2.v:
    lst = [(a, 1), (b, 1), (c, 0), (d, 0)]
    lst.sort(key = lambda a: a[0].x * (10 ** 4) + a[0].y)
    if lst[1][0] == lst[2][0]:
        print(str(lst[1][0]))
        exit()
    if lst[0][1] == lst[1][1]:
        print('Empty')
        exit()
    if lst[0][1] == lst[2][1] or lst[1][1] == lst[2][1]:
        print(str(lst[1][0]) + '\n')
        print(str(lst[2][0]))
        exit()
        
p = l1 * l2
print(str(p))
exit()
    



   