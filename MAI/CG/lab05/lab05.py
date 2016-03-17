from tkinter import *
from tkinter.ttk import *
from random import randint

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)

def alpha(al, bl, k):
    q = (1 - k) / k
    t = Point(0,0)
    a = al[0]
    b = bl[0]
    t.x = (a.x * al[1] + b.x * q * bl[1]) / (al[1] + q * bl[1])
    t.y = (a.y * al[1] + b.y * q * bl[1]) / (al[1] + q * bl[1])
    return (t, al[1] * k + bl[1] * (1 - k))

class Polynom():
    def __init__(self, k):
        self.k = k

    def __len__(self):
        return len(self.k)

    def __add__(a, b):
        t = Polynom([0 for i in range(max(len(a), len(b)))])
        for i in range(len(t)):
            if i < len(a):
                t.k[i] += a.k[i]
            if i < len(b):
                t.k[i] += b.k[i]
        return t

    def __mul__(a, b):
        if type(b) in [int, float]:
            t = Polynom([0 for i in range(len(a))])
            for i in range(len(t)):
                t.k[i] = a.k[i] * b
            return t
        else:
            t = Polynom([0 for i in range(len(a) * len(b))])
            for i in range(len(a)):
                for j in range(len(b)):
                    t.k[i + j] += a.k[i] * b.k[j]
            return t
    
    def __str__(a):
        s = ''
        for i in range(len(a)):
            if a.k[i] == 0:
                continue
            if a.k[i] > 0 and i > 0:
                s += '+'
            s += str(a.k[i])
            if i > 1:
                s += 'x^' + str(i)
            elif i == 1:
                s += 'x'

        return s

    def calc(self, x):
        r = self.k[0]
        q = x
        for i in range(1, len(self)):
            r += q * self.k[i]
            q *= x
        return r

    def draw(self):
        dx = 1
        prev = Point(0, 0)
        for i in range(500):
            new = Point(i * dx, self.calc(i * dx))
            drawline(prev, new)
            prev = new



    def Lagrange(self, pts):
        t = Polynom([])
        for j in range(len(pts)):
            w = Polynom([1])
            for i in range(len(pts)):
                if i != j:
                    q = Polynom([-pts[i].x/1000, 1/1000])
                    q = q * (1/(pts[j].x/1000 - pts[i].x/1000))
                    w = w * q
            t = t + w * pts[j].y
        return t

def drawline(a, b):
    canv.create_line(a.x, a.y, b.x, b.y, width = 2, fill = 'blue')


def randp():
    return Point(randint(20, 480), randint(20, 480))


mode = 1

near = None

def drawoval(p):
    o = canv.create_oval([p.x - r, p.y - r], [p.x + r, p.y + r], fill="black")

def reDraw():
    global cpts, pts
    canv.delete("all")        
    cpts = []         
    for p in pts:
        cpts.append(canv.create_oval([p.x - r, p.y - r], [p.x + r, p.y + r], fill="black")) 
    if mode == 1:
        Polynom([]).Lagrange(pts).draw()
    if mode == 2:
        if len(pts) < 2:
            return
        prev = pts[-1]
        for i in range(1, 100):
            t = i / 100
            q = [(pts[j], mas[j]) for j in range(len(pts))]
            while len(q) != 1:
                p = q
                q = []
                for i in range(len(p) - 1):
                    q.append(alpha(p[i], p[i+1], t))
            newp = q[0][0]
            if i != 1:
                drawline(prev, newp)
            prev = newp
        drawline(prev, pts[0])

def nearpoint(p):
    for i in range(len(pts)):
        if (p.x - pts[i].x) ** 2 + (p.y - pts[i].y) ** 2 < 20:
            return i
    return None

def onMousePress(event):
    global near
    print('press')
    p = Point(event.x, event.y)
    print(event.x, event.y)
    near = nearpoint(p)
    return near
   
def onMouseMove(event):
    if near != None:
        canv.coords(cpts[near], event.x-r, event.y-r, event.x+r, event.y+r)
        pts[near] = Point(event.x, event.y)
        reDraw()

    print('move')
def onMouseRelease(event):
    reDraw()
    print('release')

def onDoubleClick(event):
    pts.append(Point(event.x, event.y))
    mas.append(1)
    near = len(pts) - 1
    reDraw()

def onRightRelease(event):
    n = nearpoint(Point(event.x, event.y))
    if n != None:
        del pts[n]
        del mas[n]
    reDraw()

def mode1(event):
    global mode
    mode = 1
    reDraw()

def mode2(event):
    global mode
    mode = 2
    reDraw()

def buf(event):
    if near != None:
        mas[near] += 1
        reDraw()

def debuf(event):
    if near != None and mas[near] > 0:
        mas[near] -= 1
        reDraw()


root = Tk()

root.bind('<ButtonPress>', onMousePress)
root.bind('<B1-Motion>', onMouseMove)
root.bind('<B1-ButtonRelease>', onMouseRelease) 
root.bind('<B3-ButtonRelease>', onRightRelease) 
root.bind('<Double-Button-1>', onDoubleClick)
root.bind('l', mode1)
root.bind('b', mode2)
root.bind('q', exit)
root.bind('+', buf)
root.bind('=', buf)
root.bind('-', debuf)
canv = Canvas(root, width=500, height=500, bg="lightblue")
canv.pack()     
pts = [randp() for i in range(5)]
mas = [1 for i in range(len(pts))]
print('\n'.join(list(map(str, pts))))
r = 5
reDraw()


root.mainloop()




