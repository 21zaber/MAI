from math import sqrt


def get_sq(a):
    return int(sqrt(a-1)) ** 2

num = int(input())

sqs = [i ** 2 for i in range(1, 500)]
sums = [0 for i in range(32)]
for i in range(1, len(sums)):
    sums[i] = i + sums[i-1]

def get_ans(n, k, sq):
    ans = []

    ans.append(n - sq)

    n -= ans[0]

    t = 1
    for i in range(k-2):
        if t == ans[0]:
            t += 1
        ans.append(t)
        n -= t
        t += 1

    if n <= ans[-1]:
        return None

    if n != ans[0]:
        ans.append(n)
    elif n > ans[-1]+2:
        ans[-1] += 1
        ans.append(n-1)
        if ans[-1] == ans[-2]:
            return None
    else:
        return None
    return ans


for i in range(num):
    n, k = map(int, input().split())

    if n < sums[k]:
        print('NO')
        continue

    for sq in sqs:
        if sq >= n:
            print('NO')
            break
        ans = get_ans(n, k, sq)
        if ans is None:
            continue
        else:
            print('YES')
            print(' '.join(list(map(str, ans))))
            break
