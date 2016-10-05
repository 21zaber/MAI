inp = open('choose.in', 'r').read().split('\n')
incount = 0
out = open('choose.out', 'w')

def input ():
    global incount
    incount += 1
    return inp[incount - 1]

def print(t):
    out.write(t)
    
    
n, k, m = map(int, input().split())

d = [[0 for i in range(n + 1)] for j in range(k + 1)]

for i in range(1, n + 1):
    d[1][i] += 1
    
for l in range(1, k + 1):
    for r in range(n + 1, 0, -1):
        for q in range(r + 1, n + 1):
            d[l][r] += d[l - 1][q]
            
#for i in range(1, k + 1):
#    for j in range(1, n + 1):
#        print(d[i][j], end = ' ')
#    print()

a = 1
ans = []
t = m
for p in range(k, 0, -1):
    for i in range(a, n + 1):
        if d[p][i] > t :
            break        
        t += -d[p][i]
    a = i + 1
    ans.append(i)
    
#ans.append(t)
    
for i in ans:
    print(str(i) + ' ')