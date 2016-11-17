#!/usr/bin/python3.5
from random import randint



def gen1(total, n, min_s, max_s, fout="test"): # only alloc
    output = open(fout, "w")

    output.write("{}\n{}\n".format(total, n))
    for i in range(n):
        output.write("0 {}\n".format(randint(min_s, max_s)))

    output.close()

def gen2(total, n, min_s, max_s, fout="test"): # only alloc
    output = open(fout, "w")

    output.write("{}\n{}\n".format(total, n+1))
    t = 0
    for i in range(n):
        if randint(0, 99) < 30 and t > 0:
            output.write("1 {}\n".format(randint(0, t-1)))
            t -= 1
        else:
            output.write("0 {}\n".format(randint(min_s, max_s)))
            t += 1

    output.write("2 2\n")

    output.close()

def gen3(total, min_s, msx_s, fout="test"):
    output = open(fout, "w")

    output.write("{}\n{}\n".format(total, n+1))
    l = []
    mem = 0
    for i in range(n):
        bl = randint(min_s, max_s)
        output.write("0 {}\n".format(bl))
        l.append()
        

    output.write("2 2\n")

    output.close()

class Generator():
    def __init__(self, total):
        self.total = total
        self.cmds = []

    def __str__(self):
        s = "{}\n{}\n".format(self.total, len(self.cmds))
        for cmd in self.cmds:
            s += "{} {}\n".format(cmd[0], cmd[1])
        return s

    def add(self, a, b):
        self.cmds.append((a, b))

def gen(total, min_s, max_s, elem_sz):
    g = Generator(total)
    mem = 0
    cnt = 0
    while mem + max_s+ elem_sz < total:
        a = randint(min_s, max_s)
        g.add(0, a)
        mem += a+elem_sz
        cnt += 1

    if total - mem-elem_sz > 0:
        g.add(0, total - mem- elem_sz)
        cnt += 1


    t = []
    
    for i in range(cnt-1, -1, -2):
        g.add(1, i)
        t.append(g.cmds[i][1])


    for i in t:
        g.add(0, i)

    
    return g


#for i in range(10):
#    gen2(1000*1000*1000, 70*1000, 100*1000*1000, 1000*1000*1000, fout="gtest{}".format(i))

for i in range(10):
    g = gen(10*1000*1000, 1*1000, 1010, 32)
    fname = "gtest{}".format(i)
    fout = open(fname, "w")
    fout.write(str(g))
    fout.close()


