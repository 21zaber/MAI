a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

def square(a):
    return a[0] ** 2 + a[1] ** 2 == a[2] ** 2

if not square(a):
    print(0)
    exit()

if not square(b):
    print(0)
    exit()

if a == b:
    print(1)
else :
    print(0)
