n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    s = 0
    while a > 0:
        if a % 2 == 1:
            s += b
        a = a // 2
        b *= 2
    print(s)

