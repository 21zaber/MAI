

t = int(input())

sqs = [i ** 2 for i in range(1, 700)]
sums = [0 for i in range(32)]
for i in range(1, len(sums)):
    sums[i] = i + sums[i-1]

for i in range(t):
    n, k = map(int, input().split())

    print(n, k)
    if n < sums[k]:
        print('NO')
        continue

    c = n - sums[k-2]

    for sq in sqs:
        if sq >= n:
            print('NO')
            break
        f = n - sq
        if f > c:
            continue
        c -= f
        if c == f or n-sq <= k-2:
            continue
        if sq <= k-2:
            ans = []
        ans = get_ans(n, k, sq)
        if ans is None:
            continue
        else:
            print('YES')
            #print(sq)
            print(' '.join(list(map(str, ans))))
            break



