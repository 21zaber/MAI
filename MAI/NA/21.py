from math import sqrt, e

def rf(x):
    return ((e ** x + 0.5) ** 2.0) / 9 - 1.0

def f(x):
    return 3 * sqrt(x+1) - e ** x - 0.5

def f1(x):
    return  3 / (2 * sqrt(x+1)) - e ** x

from random import random as rand

x = -0.7
eps = 0.00000001
q = 0.7

print('Simple iteration method:')

iter_n = 1
fl = True
while fl and iter_n < 1000:
    nx = rf(x)
    print('{}: {}'.format(iter_n, nx))
    fl = q / (1 - q) * abs(x - nx) > eps
    x = nx
    iter_n += 1

print('Answer: {}'.format(x))

x = -0.7
print()
print('Newtons method:')

iter_n = 1
fl = True
while fl and iter_n < 1000:
    nx = x - f(x)/f1(x)
    print('{}: {}'.format(iter_n, nx))
    fl = q / (1 - q) * abs(x - nx) > eps
    x = nx
    iter_n += 1


print('Answer: {}'.format(x))
