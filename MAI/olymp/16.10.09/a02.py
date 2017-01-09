n, s = list(map(int, input().split()))
m = list(map(int, input().split())) 
sums = [m[0]]
for i in m[1:]:
    sums.append(sums[-1] + i)

def getsum(l, r):
    print('sum', l, r)
    if l == 0:
        return sums[r]
    return sums[r] - sums[l-1]


def check(leng):
    print('check', leng)
    if leng == 0 and getsum(0, n-1) <= s:
        return (True, 0, 0)

    for i in range(leng+1):
        l = i
        r = leng - i - 1
        if getsum(l, r) <= s:
            return (True, l, r)
    return (False, )





l, r = -1, n

while r - l > 1:
    mm = (l + r + 1) // 2
    if check(mm)[0]:
        r = mm
    else:
        l = mm

#print('l {} r {} m {}'.format(l, r, mm))

print(n - r)
ans = check(r)
print(ans[1], ans[2])


