n,m = map(int, input().split())

from random import randint


print(n,m)
for i in range(n):

    for j in range(m):
        c = randint(0, 1)
        if c == 0:
            c = '.'
        else:
            c = '+'
        print(c, end='')
    print()
