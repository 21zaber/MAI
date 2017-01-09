n = int(input())

t = 0

def check(a):
    q = list(map(int, list(str(a))))
    for i in range(1, len(q)):
        if abs(q[i] - q[i-1]) != 1:
            return False
    return True

def inc(a, n = 1):
    q = [0] + list(map(int, list(str(a))))
    if n == len(q):
        return False
    t = inc(a, n+1)
    if t != False:
        return t
    if n != 1 and q[n] > q[n-1]:
        return False
    if n != 1 and q[n] > 7:
        return False
    if n == 1:
        q[n] += 1
        if q[n] > 9:
            q[n-1] += 1
            q[n] = 0
    else:
        q[n] += 2

    for i in range(n+1, len(q)):
        q[i] = min((q[i-1] + 1) % 10, (q[i-1] - 1) % 10)

    t = 0
    b = 1
    for i in q[::-1]:
        t += b * i
        b *= 10
    return t

for i in range(n):
    t = inc(t)

print(t)
