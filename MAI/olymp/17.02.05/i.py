n = int(input())

l = [str(i) for i in range(1, n+1)]

l.sort()

c = 0

for i, a in enumerate(l):
    for b in l[i+1:]:
        if int(a) > int(b):
            c += 1

print(c)
