num = 290000

from math import sqrt

def is_sq(a):
    return int(sqrt(a)) ** 2 == a

def check(a):
    for i in a:
        if i <= 0:
            return False
    return True

for i in range(num):
    try:
        s = input()
        n, k = map(int, s.split())
        ans = input()
        if ans[0] == 'Y':
            t = list(map(int, input().split()))
            if len(set(t)) == k and sum(t) == n and is_sq(sum(t[1:])) and check(t):
                continue
            print(n, k, t)
    except:
        print(s)
    
