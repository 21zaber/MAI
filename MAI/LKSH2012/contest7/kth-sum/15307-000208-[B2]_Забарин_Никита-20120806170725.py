inp = open('num2part.in', 'r').read().split('\n')
incount = 0
out = open('num2part.out', 'w')

def input ():
    global incount
    incount += 1
    return inp[incount - 1]

def print(t):
    out.write(t)

n, r = map(int, input().split())

d = [[0 for i in range(n + 2)] for j in range(n + 2)]

for i in range(n + 1):
    d[0][i] = 1
    
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        d[i][j] = d[i - j][j] + d[i][j + 1]
    
def ans (q, s, i):
    global n
    if q != 0:
        while s >= d[q - i][i]:
            s += -d[q - i][i]
            i += 1
        q += -i
        if q != 0:
            print(str(i) + '+')
        else:
            print(str(i))
        ans(q, s, i)
        
ans(n, r, 1)
    
#1 1 1 1
#1 2 2
#1 3
#2 2
#4