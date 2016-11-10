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

for i in range(10):
    gen2(1000*1000*1000, 70*1000, 100*1000*1000, 1000*1000*1000, fout="gtest{}".format(i))



