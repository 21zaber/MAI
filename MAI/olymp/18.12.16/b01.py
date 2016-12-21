n = int(input())

from math import sqrt

n *= 6

def area(r):
    return 1 + 3 * r * (r+1)

def radius(n):
    if n < 1:
        return -1
    return int(-0.5 + sqrt((12 * n - 3) / 6)) + 1

mr = radius(n)

cakes = []

cnt = 0
tn = n
r = radius(n)

#print(r)

while r >= 0:
    #print(r, area(r))
    cn = tn // area(r)
    tn %= area(r)
    cnt += cn


    if cn > 0:
        cakes.append((r, cn))

    
    r = min(r-1, radius(tn))

    
print(6)
for i in cakes:
    for j in range(i[-1]):
        print(i[0]+1, end= ' ')




