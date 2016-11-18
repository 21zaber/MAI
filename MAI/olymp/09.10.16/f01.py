n = int(input())


def r(a):
    if a == 0:
        return ''
    if a == 1:
        return '1'
    if a == 2:
        return '11'
    if a % 2 == 0:
        return '[{}]'.format(r(a // 2))
    else:
        return '1' + r(a - 1)

print(r(n))
#print(len(r(n)))
