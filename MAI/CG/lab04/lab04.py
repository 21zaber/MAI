from mymodule import app, ImportTexture
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin, cos, pi
from random import random, seed

seed()


def Z (x, y):
    return sin(0.3 * x) + sin(0.7 * y) * sin(0.5 * y) 
    #return (abs(20 - x * x + y * y) ** 0.5) / 3  

def randpos():
    return random() * 10 - 5

class Surface():
    def N(self, x, y):
        dzdx = self.func(x + 1, y) - self.func(x, y)
        dzdy = self.func(x, y + 1) - self.func(x, y)
        x, y, z = -dzdx, -dzdy, 1
        ab = (x**2 + y**2 + z**2) ** 0.5
        return (x / ab, y / ab, z / ab)  

    def __init__(self, texture = 'grass.png', func = Z):
        self.texture = texture
        self.func = func
        dx = dy = 0.5
        self.listid = glGenLists(1)
        glNewList(self.listid, GL_COMPILE)
        glBegin(GL_QUADS)
        n = 10
        for xi in range(-n, n):
            for yi in range(-n, n):
                x, y = xi * dx, yi * dy
                xx, yy = x + dx, y + dy
     
                glNormal3fv(self.N(x, y))
                glTexCoord2f(x, y)
                glVertex3f(x, y, Z(x, y))
                
                glNormal3fv(self.N(xx, y))
                glTexCoord2f(xx, y)
                glVertex3f(xx, y, Z(xx, y))
     
                glNormal3fv(self.N(xx, yy))
                glTexCoord2f(xx, yy)
                glVertex3f(xx, yy, Z(xx, yy))
     
                glNormal3fv(self.N(x, yy))
                glTexCoord2f(x, yy)
                glVertex3f(x, yy, Z(x, yy))  
        glEnd()     
        glEndList() 
        self.texid = ImportTexture(texture)

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glCallList(self.listid)


class Tree():
    def cylinder(self, x, y, z, height, r):
        def vertex(a, h):
            glTexCoord2f(r * cos(a) + x, r * sin(a) + y)
            glVertex3f(r * cos(a) + x, r * sin(a) + y, h + z)
            glNormal3f(r * cos(a), r * sin(a), 0)
        
        n = 10
        da = pi / n
        glBegin(GL_QUADS)
        for ai in range(n * 2):
            a = ai * da
            aa = a + da
            h = 0
            hh = height

            vertex(a, h)
            vertex(aa, h)
            vertex(aa, hh)
            vertex(a, hh)
        glEnd()

    def sphere(self, x, y, z, r):
        def vertex(a, b):
            vx, vy, vz = r * cos(a) * cos(b), r * cos(a) * sin(b), r * sin(a)
            glTexCoord2f(vx + x, vy + y)
            glVertex3f(vx + x, vy + y, vz + z)
            glNormal3f(vx, vy, vz)
        
        n = 10
        d = pi / n
        glBegin(GL_QUADS)
        for ai in range(2 * n):
            for bi in range(2 * n):
                a, b = ai * d, bi * d
                aa, bb = a + d, b + d

                vertex(a, b)
                vertex(aa, b)
                vertex(aa, bb)
                vertex(a, bb)
        glEnd()

    def __init__(self):
        self.listid = glGenLists(1)
        x, y = random() * 10 - 5, random() * 10 - 5
        k = random() * 0.5 + 0.3
        glNewList(self.listid, GL_COMPILE)
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (0.3, 0.3, 0.3, 0.8))
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.6, 0.6, 0.3, 0.8))
        self.cylinder(x, y, Z(x, y) - 0.1, 0.6 * k, 0.09 * k)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.2, 0.8, 0.0, 0.4))
        self.sphere(x, y, Z(x, y) - 0.1 + 0.6 * k, 0.3 * k) 

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (0.0, 0.0, 0.0, 0.8))
        glEndList() 
        self.texid = ImportTexture('mtree.png')
    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glCallList(self.listid) 


class Cloud():                      
    def sphere(self, x, y, z, r):
        k = random()
        def vertex(a, b):
            vx, vy, vz = r * cos(a) * cos(b), r * cos(a) * sin(b), r * sin(a) * k
            glTexCoord2f(vx + x, vy + y)
            glVertex3f(vx + x, vy + y, vz + z)
            glNormal3f(vx, vy, vz)
        
        n = 7
        d = pi / n
        glBegin(GL_QUADS)
        for ai in range(2 * n):
            for bi in range(2 * n):
                a, b = ai * d, bi * d
                aa, bb = a + d, b + d

                vertex(a, b)
                vertex(aa, b)
                vertex(aa, bb)
                vertex(a, bb)
        glEnd()                     

    def __init__(self):
        self.texid = ImportTexture("cloud.png")
        self.listid = glGenLists(1)
        x, y, z = randpos() * 5, randpos() * 5, random() * 20 + 5
        glNewList(self.listid, GL_COMPILE)
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.8, 0.8, 0.8, 0.8))
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (0.8, 0.8, 0.8, 0.8))
        for i in range(10):
            cx, cy, cz, r = random() * 1.6, random() * 1.6, random(), random() * 2
            self.sphere(x + cx, y + cy, z + cz, r)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (0.0, 0.0, 0.0, 0.8))
        glEndList()

    def draw(self):
        glBindTexture(GL_TEXTURE_2D, self.texid)
        glCallList(self.listid) 
        


app.addobj(Surface())
for i in range(15):
    app.addobj(Tree())

for i in range(20):
    app.addobj(Cloud())

app.run()
