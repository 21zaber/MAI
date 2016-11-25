#!/usr/bin/python3.5

def check(n):
    ans = n + 1
    for t in range(4 ** n+1):

        a, b, c, d = 0, 0, 0, 0
        for i in range(n):
            if t % 4 == 0:
                a += i + 1
            elif t % 4 == 1:
                b += i + 1
            elif t % 4 == 2:
                c += i + 1
            else:
                d += 1
            t //= 4
        
        if a*b*c > 0 and 2 * max([a, b, c]) < sum([a, b, c]):
            #print(a, b, c)
            ans = min(d, ans)
            if ans == 0:
                print(a, b, c)
                break

    return ans


#for n in range(3, 10):
#    print(n, check(n))
#

t = 100
for a in range(t):
    for b in range(a+1, t):
        for c in range(b+1, t):
            for d in range(c+1, 100):
                for e in range(d+1, 100):
                    if a+b <= c and a+c <= d and b+c <=d and a+d <= e and b+d <= e and c+d <= e:
                        print(a, b, c, d, e)



