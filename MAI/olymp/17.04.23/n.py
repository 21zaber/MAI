n = int(input())
x, y = map(int, input().split())

def getcoord(n, x, y):
    if n == 0:
        return ''

    ans = '0'
    t = 2 ** (n-1)
    if y <= t:
        ans = '0'
    elif y > t * 3:
        ans = '2'
    elif x <= t:
        ans = '1'
    else:
        ans = '3'

    #print("{} {}: {}".format(x, y, ans))
   #print(t)

    if n == 1:
        return ans
    else:
        if ans == '0':
            return ans + getcoord(n-1, t + 1 - y, x)
        if ans == '1':
            return ans + getcoord(n-1, x, y - t)
        if ans == '2':
            return ans + getcoord(n-1, t + 1 - (y - 3*t), x)
        if ans == '3':
            return ans + getcoord(n-1, x - t, y - t)

ans = ""
lstc = getcoord(n, x, y)

mxx = 2 ** n
mxy = 2 ** (n+1)

for i in input():
    nx, ny = x, y
    if i == "U":
        nx -= 1
    if i == "D":
        nx += 1
    if i == "R":
        ny += 1
    if i == "L":
        ny -= 1
    nx = max(1, nx)
    ny = max(1, ny)
    nx = min(mxx, nx)
    ny = min(mxy, ny)
    newc = getcoord(n, nx, ny)
    if newc == lstc:
        #print('N', end='')
        ans += 'N'
    else:
        #print('Y', end='')
        ans += 'Y'
    x, y, lstc = nx, ny, newc

print(ans)

#while True:
#    x, y = map(int, input().split())
#for x in range(1, 2 ** n +1):
#    for y in range(1, 2 ** (n+1) +1):
#        print(x, y, getcoord(n,x,y))
