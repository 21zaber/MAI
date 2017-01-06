a = ['a', 'b', 'c', 'd']

import sys

def foo(i, j):
    print('Is {} < {}?'.format(a[i], a[j]))
    sys.stdout.flush()
    t = input()
    return t[0] == 'Y'

def ans(i):
    print('Value {} is non-extremal.'.format(a[i]))
    exit(0)

ab, bc, ac = foo(0, 1), foo(1, 2), foo(0, 2)



if ab:
    # b > a
    if bc:
        # c > b
        ans(1)
    elif ac:
        # c < b, c > a
        ans(2)
    else:
        # c < b, c < a
        ans(0)

# b < a
if ac:
    # c > a
    ans(0)
elif bc:
    # c < a, c > b
    ans(2)
else:
    ans(1)

