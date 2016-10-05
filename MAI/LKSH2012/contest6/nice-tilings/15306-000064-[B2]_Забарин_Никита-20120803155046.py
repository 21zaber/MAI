inp = open('tilings.in', 'r').read().split('\n')
incount = 0
out = open('tilings.out', 'w')

def input ():
    global incount
    incount += 1
    return inp[incount - 1]

def print(t):
    out.write(t)


n, m = map(int, input().split())

if n > m:
    t = n
    n = m
    m = t
    
m1 = range(2 ** n)
dp = [[0 for i in range(2 ** n + 1)] for j in range(m + 1)]

for i in range(2 ** n):
    dp[1][i] += 1

def check(m1, m2):
    mm1 = list(bin(m1)[2:])
    mm2 = list(bin(m2)[2:])
    for i in range(n - len(mm1)):
        mm1 = ['0'] + mm1
    for i in range(n - len(mm2)):
        mm2 = ['0'] + mm2    
        
    for i in range(1, len(mm1)):
        if mm1[i] == mm2[i] and mm1[i - 1] == mm2[i - 1] and mm1[i] == mm1[i - 1]:
            return False
    return True
    
for i in range(1, m):
    m2 = [] 
    for mask1 in range(2 ** n):       
        for mask2 in m1:
            if check(mask1, mask2):
                dp[i + 1][mask1] += dp[i][mask2]
                m2.append(mask2)
    m1 = m2
    m1.sort()
    for i in range(len(m1) - 1, 0, -1):
        if m1[i] == m1[i - 1]:
            del(m1[i])
        
        
print(str(sum(dp[m])))