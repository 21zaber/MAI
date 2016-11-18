n, s = list(map(int, input().split()))
m = list(map(int, input().split())) 
sums = [m[0]]
for i in m[1:]:
    sums.append(sums[-1] + i)

#print(sums)

def getsum(l, r):
   #print('getsum', l, r)
    if l == 0:
        return sums[r]
    return sums[r] - sums[l-1] 


l, r = -1, n

def check(ll):
   #print('check', ll)
    if ll == 0 and sums[n-1] <= s:
        return True
    for i in range(ll):
        if getsum(i, n - ll + i - 1) <= s:
            return True
    return False

while r - l > 1:
  #  print('l {} r {}'.format(l, r))
    mm = (l + r + 1) // 2
    print('l {} r {} m {}'.format(l, r, mm))
    if check(mm):
        r = mm
    else:
        l = mm

#FIXME

#print('l {} r {} m {}'.format(l, r, mm))
l = r

#print('l', l)
if l == n:
    print(-1)
    exit()

if l == n-1 and not check(n):
    print(-1)
    exit()

print(n - l)

if l == 0:
    print(0, 0)
    exit()

for i in range(l+1):
   #print('===========')
   #print(i)
   #print('l: {} r: {}'.format(i, l-i))
   #print(getsum(i, n - l + i-1))
    if getsum(i, n - l + i-1) <= s:
        print(i, l-i)
        break
