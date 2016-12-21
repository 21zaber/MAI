
n = 7

from math import sqrt

def check(a, qwe = 4):
    t = str(a)
    for j in range(qwe, 10):
        if str(j) in t:
            return False
    return True      

def foo(a):
    ans = []
    t = a
    for i in range(2, int(sqrt(a))):
        if t % i == 0:
            ans.append(i)
        while t % i == 0:
            t //= i
    if t > 1:
        ans.append(t)
    return list(set(ans))

test = set()
test2 = set()

for i in range(10 ** n):
    if not check(i, 2):
        continue
    t = i ** 2
    print(i, t, check(t), foo(i))
    if check(t):
        test.update(foo(i))
    else:
        test2.update(foo(i))

print(test)
print(test2)
print(test - test2)
print(test2 - test)

exit()

for i in range(10**(n-1), 10 ** n):
    if not check(i, 2):
        continue

    s = int(sqrt(i))
    if s ** 2 == i:
        if check(s):
            print(i, s, foo(i))


