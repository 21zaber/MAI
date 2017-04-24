
n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())

    ans = []
    # cd - lie
    if a < c or a > d:
        mn = a
    else:
        mn = d+1
    if b > d or b < d:
        mx = b
    else:
        mx = c-1

    if mx >= mn:
        ans.append((mn, mx))

    # b - lie
    mn = max(a, c, b+1)
    mx = d
    if mx >= mn:
        ans.append((mn, mx))

    # cd - right
    mn = c
    mx = min(d, a-1, b)
    if mx >= mn:
        ans.append((mn, mx))

#    print(ans)

    if len(ans) > 1:
        print("Indeterminancy")
    elif len(ans) == 0:
        print("Absurd")
    else:
        print(ans[0][0], ans[0][1])

