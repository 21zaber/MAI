inp = open('coolnumbers.in', 'r').read().split('\n')
incount = 0
out = open('coolnumbers.out', 'w')

def input ():
    global incount
    incount += 1
    return inp[incount - 1]


l, r, k = input().split()
k = int(k)

def sum (n, flag):
    d = [[[0 for i in range(2)] for j in range(k)] for q in range(len(n) + 1)]
    for i in range(int(n[0])):
        d[1][i % k][1] += 1
    d[1][int(n[0]) % k][0] += 1
    for l in range(len(n)):
        for r in range(k):
            for i in range(10):
                d[l + 1][(i + r) % k][1] += d[l][r % k][1]
            for i in range(int(n[l])):
                d[l + 1][(i + r) % k][1] += d[l][r % k][0]
            d[l + 1][(int(n[l]) + r) % k][0] += d[l][r % k][0]
    if flag:
        return d[len(n)][0][1] + d[len(n)][0][0]
    else:
        return d[len(n)][0][1]

out.write(str((sum(r, True) - sum(l, False))))
    
            