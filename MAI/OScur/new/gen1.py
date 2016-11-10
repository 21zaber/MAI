#!/usr/bin/python3.4
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
    mem = 0
    t = 0
    blocks = []
    for i in range(n):
        f = True
        while f:
            if randint(0, 100) < 10 and t > 0:
                idx = randint(0, t-1)
                mem -= blocks[idx]
                del blocks[idx]
                output.write("1 {}\n".format(idx))
                t -= 1
                f = False
            elif mem + min_s < total:
                bl = randint(min_s, max_s)
                blocks.append(bl)
                mem += bl
                output.write("0 {}\n".format(bl))
                t += 1
                f = False

    output.write("2 2\n")

    output.close()


def gen3(total, n, min_s, max_s, fout="test"): # only alloc
    output = open(fout, "w")

    output.write("{}\n{}\n".format(total, n+2))
    mem = 0
    t = 0
    blocks = []
    op = 0
    while mem + min_s < total:
        bl = min_s
        blocks.append(bl)
        mem += bl
        output.write("0 {}\n".format(bl))
        t += 1
        op += 1

    for idx in range(0, len(blocks), 3):
        mem -= blocks[idx]
        output.write("1 {}\n".format(idx))
        t -= 1
        op += 1

    for idx in range(1, len(blocks), 3):
        mem -= blocks[idx]
        output.write("1 {}\n".format(idx))
        t -= 1
        op += 1

    blocks= [blocks[i] for i in range(len(blocks)) if i % 3 == 2]

    output.write("2 2\n")

    for i in range(n - op):
        f = True
        while f:
            if randint(0, 100) < 10 and t > 0:
                idx = randint(0, t-1)
                mem -= blocks[idx]
                del blocks[idx]
                output.write("1 {}\n".format(idx))
                t -= 1
                f = False
            elif mem + min_s < total:
                bl = randint(min_s, max_s)
                blocks.append(bl)
                mem += bl
                output.write("0 {}\n".format(bl))
                t += 1
                f = False

    output.write("2 2\n")

    output.close()

for i in range(10):
    gen3(1*1*1000*1000, 10*1000, 1*1000, 1*10*1000, fout="gtest{}".format(i))



