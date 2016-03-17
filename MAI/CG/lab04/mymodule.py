from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sqrt, sin, cos, pi
from PIL.Image import open as openimage


def OnMouseMove(x, y):
    app._OnMouseMove(x, y)

def OnKeyPress(k, b, c):
    app._OnKeyPress(k, b, c)

def OnReDraw():
    app._OnReDraw()

class App():
    class Player:
        def __init__(self):
            self.x = 0.6; self.y = 0.6; self.z = 0.6
            self.yaw = 0.0
            self.pitch = 0.0
            self.speed = 0.1
        def move_forward(self, k = 1):
            self.x += k * cos(self.yaw) * cos(self.pitch) * self.speed
            self.y += k * sin(self.yaw) * cos(self.pitch) * self.speed
            self.z += k * sin(self.pitch) * self.speed
        def move_right(self, k = 1):
            self.x += k * sin(self.yaw) * self.speed
            self.y -= k * cos(self.yaw) * self.speed
        def move_left(self, k = 1):
            self.move_right(-k)
        def move_back(self, k = 1):
            self.move_forward(-k)
        def move_up(self):
            self.z += self.speed    

    def _OnKeyPress(self, k, b, c):
        global looping
        if k == b'q':
            self.looping = False
        if k == b'w':
            self.player.move_forward()
        if k == b's':
            self.player.move_back()
        if k == b'a':
            self.player.move_left()
        if k == b'd':
            self.player.move_right()
        if k == b' ':
            self.player.move_up();

    def _OnMouseMove(self, x, y):
        dx = self.prevx - x
        dy = self.prevy - y
        self.player.yaw +=   dx * 0.01
        self.player.pitch += dy * 0.01
        if self.player.pitch > pi / 3: 
            self.player.pitch = pi / 3
        if self.player.pitch < -pi / 3: 
            self.player.pitch = -pi / 3
        self.prevx = x
        self.prevy = y

    def setuplight(self):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  (1, 1, 1, 1))
        glLightfv(GL_LIGHT0, GL_AMBIENT,  (0.2, 0.2, 0.2, 1))
        glLightfv(GL_LIGHT0, GL_POSITION, (100, 100, 100, 0))

    def settings(self):
        glClearColor(.4, .5, .6, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, glutGet(GLUT_WINDOW_WIDTH) / glutGet(GLUT_WINDOW_HEIGHT), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.player.x, self.player.y, self.player.z,
                  self.player.x + cos(self.player.yaw) * cos(self.player.pitch),
                  self.player.y + sin(self.player.yaw) * cos(self.player.pitch),
                  self.player.z + sin(self.player.pitch),
                  0, 0, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glEnable(GL_TEXTURE_2D)
        self.setuplight() 

    def _OnReDraw(self):
        self.settings()
        for obj in self.objects:
            obj.draw()

        glutSwapBuffers()

    def addobj(self, obj):
        self.objects.append(obj)

    def run(self):
        while(self.looping):
            glutMainLoopEvent()
            glutPostRedisplay()

    def __init__(self):
        self.looping = True
        self.player = self.Player()
        self.prevx, self.prevy = 0, 0
        self.objects = []


        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutCreateWindow('')
        glutDisplayFunc(OnReDraw)
        glutKeyboardFunc(OnKeyPress)
        glutPassiveMotionFunc(OnMouseMove) 


def ImportTexture(filename):
    global texdict
    if filename in texdict:
        return texdict[filename]
    img = openimage(filename)
    imx, imy = img.size[:2] 

    try:
        imstr = img.tostring('raw', 'RGBA', 0, -1)
    except SystemError:
        imstr = img.tostring('raw', 'RGBX', 0, -1)
    
    imid = glGenTextures(1)
    
    glBindTexture(GL_TEXTURE_2D, imid)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    #glTexImage2D(GL_TEXTURE_2D, 0, 3, imx, imy, 0, GL_RGBA, GL_UNSIGNED_BYTE, imstr)
        
    gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, imx, imy, GL_RGBA, GL_UNSIGNED_BYTE, imstr)
    texdict[filename] = imid
    return imid

texdict = {}
app = App()
