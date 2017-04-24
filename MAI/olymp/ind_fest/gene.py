
from random import randint

n = 10000
print(n*29)
for i in range(n):
    num = randint(1, 10000)
    #l = sum([i+1 for i in range(k)])
    l = 1
    r = 100000
    for i in range(2, 31):
        print(num, i)

