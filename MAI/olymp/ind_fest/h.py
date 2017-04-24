
segs_idx = 0

class seg():
    def __init__(self, x, y, x2, y2):
        global segs_idx
        if x2 < x:
            x, x2 = x2, x
            y, y2 = y2, y

        self.id = segs_idx
        segs_idx += 1
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def read():
        return seg(*list(map(int, input().split())))

    def gety(self, x):
        if x < self.x or x > self.x2:
            return None
        return ((x - self.x) * self.y2 + (self.x2 - x) * self.y) / (self.x2 - self.x)

    def getx(self):
        if self.y < self.y2:
            return self.x
        else:
            return self.x2

    def key(self):
        return self.x 
    
    def __hash__(self):
        return self.id

    def __str__(self):
        return "{} {} {} {}".format(self.x, self.y, self.x2, self.y2)

csegs = set()
cpos = 0

def move(xf, xt):
    if xf > xt:
        moveleft(xf, xt)
    else:
        moveright(xf, xt)

def moveright(xf, xt):
    global csegs, cpos, segs
    if cpos == -1:
        cpos += 1

    while cpos < len(segs) and segs[cpos].x <= xt:
        if segs[cpos].x2 >= xt:
            csegs.add(segs[cpos])
        else:
            csegs.discard(segs[cpos])
        cpos += 1

def moveleft(xf, xt):
    global csegs, cpos, segs
    if cpos == len(segs):
        cpos -= 1

    while cpos > 0:
        if segs[cpos].x < xt and segs[cpos].x2 > xt:
            csegs.add(segs[cpos])
        else:
            csegs.discard(segs[cpos])
        cpos -= 1

n = int(input())
segs = [seg.read() for i in range(n)]

x0 = int(input())

segs.sort(key=lambda x:x.key())

inf = 10**10

y0 = inf

move(-inf, x0)
while len(csegs) > 0:
    print(x0, y0, csegs)
    best = None
    mx = -inf
    for sg in csegs:
        c = sg.gety(x0)
        if c >= mx and c <= y0:
            mx = c
            best = sg

    if best is None:
        break

    csegs = set()
    cpos = 0
    
    move(0, best.getx())
    x0 = best.getx()
    y0 = min(best.y, best.y2)

print(x0)


