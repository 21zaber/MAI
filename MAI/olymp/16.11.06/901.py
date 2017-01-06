n, k = map(int, input().split())

l = list(map(int, input().split()))

d = {}

s = sum(l[:k])
print(s, end=' ')

for i in l[:k]:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

def minkey():
    return list(d.keys())[0]

def delone(mk):
    if d[mk] == 1:
        del d[mk]
    else:
        d[mk] -= 1

for i in range(k, n):
    mk = minkey()
    if l[i] > mk:
        s += l[i] - mk
        delone(mk)
        if l[i] in d:
            d[l[i]] += 1
        else:
            d[l[i]] = 1
    print(s, end=' ')

print()
