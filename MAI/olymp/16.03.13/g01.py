

n = int(input())

d = list(map(int, input().split()))

d.sort(reverse = True)

t = []

for i in d:
    p = -1
    for j in range(len(t)):
        if t[j] > i:
            if p < 0 or (p >= 0 and t[j] < t[p]):
                p = j    

    if p >= 0:
        t[p] = i
    else:
        t.append(i)

print(len(t))

