from math import sqrt, log
from copy import deepcopy as copy

def rf(x):
    x1 = sqrt(2 * log(x[1]) + 1)
    x2 = (x[0] ** 2 + 3) / (3 * x[0])
    return [x1, x2]

def end(a, b):
    return max([abs(a[i] - b[i]) for i in range(len(a))])

x = [1, 1]
q = 0.5
eps = 0.001

print('Simple iteration method:')

fl = True
iter_n = 1
while fl and iter_n < 1000:
    nx = rf(x)
    print(iter_n, ': ', sep = '', end = '')
    print(nx)
    fl = q / (1 - q) * end(x, nx) > eps
    x = copy(nx)
    iter_n += 1


print('Answer: {} {}'.format(x[0], x[1]))
print()



