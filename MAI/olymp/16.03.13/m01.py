n = int(input())

a, b = 1, 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

for i in range(n):
    c, d = map(int, input().split())
    a = lcm(a, c)
    if i == 0:
        b = d
    b = gcd(b, d)

print(a, b)

