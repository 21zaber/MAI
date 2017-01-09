
def tersearch(l, r, f, par):
    eps = 0.001
    while abs(l - r) > eps:
        m1 = (l * 2 + r) / 3
        m2 = (l + 2 * r) / 3

        if f(m1, m2, par):
            l = m1
        else:
            r = m2
    return l

def check1(c, b, par):
    print(c, b)
    min1 = tersearch(0.01, 100, check2, c)
    min2 = tersearch(0.01, 100, check2, b)

    return (c / min1) < (b / min2)

def check2(min1, min2, mmax):
    print(min1, min2, mmax)
    res1 = check3(min1, mmax)
    res2 = check3(min2, mmax)
    if res1 and res2:
        return min1 > min2
    if res1:
        return False
    if res2:
        return True
    return True

def myround(t):
    if t > int(t):
        return int(t) + 1
    else:
        return t

def check3(mmin, mmax):
    ci = []
    for i in a:
        if i < mmin:
            return False
        c = myround(i / mmax)
        if c < 1 or c > k:
            return False
        t = i / c
        ci.append(c)
        if t < mmin or t > mmax:
            return False
    #print(mmin, mmax)
    #print(ci)
    return True

n, k = map(int, input().split())
a = list(map(int, input().split()))

print(tersearch(1, 100, check1, None))
    


#= min, r = max+1
#while r > l + 1:
#   m = (l + r) // 2
#   if check(m):
#       l = m
#   else
#       r = m



                                                                           
