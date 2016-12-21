
def check(a):
    t = str(a)
    for j in range(4, 10):
        if str(j) in t:
            return False
    return True      

def inc(a):
    t = str(a)
    ans = list(t)
    for i in range(len(t)-1, -1, -1):
        if t[i] == '0':
            ans[i] = '1'
            break;
        else:
            ans[i] = '0'
    return int(''.join(ans))


while True:
    n, k = map(int, input().split())
    if n * k == 0:
        exit(0)

    if n % 2 == 0:
        raise()
    
    t = n // 2
    a = 10 ** t
    if n == 1:
        a -= 1
    t = 1
    while t < k:
        a = inc(a)
        if check(a**2):
            t += 1

    print(a ** 2)

