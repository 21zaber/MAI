s = input()

d = {}

for i in list(s):
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

c = 0
m = [i[1] for i in d.items()]
m.sort()
m = m[:-2]
print(sum(m))
