def orient(s):
    a = s[0]
    b = s[1]
    c = s[2]
    vm = (b[1] - c[1]) * (b[2] - a[2]) - (b[2] - c[2]) * (b[1] - a[1])
    return vm > 0


n = int(input())
d = {}


for i in range(n):
    t = list(map(int, input().split()))
    a = (t[2] - t[0])**2 + (t[3] - t[1])**2
    b = (t[4] - t[0])**2 + (t[5] - t[1])**2
    c = (t[4] - t[2])**2 + (t[5] - t[3])**2
    
    sides = [(a, t[4], t[5]), (b, t[2], t[3]), (c, t[0], t[1])]
    sides.sort(key = lambda x: x[0])
    
    key =  (sides[0][0], sides[1][0], orient(sides))
    key2 = (sides[0][0], sides[1][0], not key[2])
    
    if key[0] == key[1]:
        key2 = (key[0], key[1], True)
        key = key2


   #if key2 in d.keys():
   #    ans.append([i + 1, d[key2][0]])
   #    del d[key2][0]
   #    if len(d[key2]) == 0:
   #        del d[key2]
   #    continue
   
    if key in d.keys():
        d[key].append(i+1)
    else:
        d[key] = [i+1]


ans = []
for key in d.keys():
    if key[0] == key[1]:
        t = d[key]
        if len(t) % 2 == 1:
            ans.append([0, t[0]])
            for i in range(1, len(t)-1, 2):
                ans.append([t[i], t[i+1]])
        else:
            for i in range(0, len(t), 2):
                ans.append([t[i], t[i+1]])

        continue
    key2 = (key[0], key[1], not key[2])
    t1 = d[key]
    if key2 in d.keys():
        t2 = d[key2]
        l = min(len(t1), len(t2))
        for i in range(l):
            ans.append([t1[i], t2[i]])
        for i in range(l, len(t1)):
            ans.append([t1[i], 0])
        for i in range(l, len(t2)):
            ans.append([t2[i], 0])
        d[key2] = []
        d[key] = []

    else:
        for i in range(len(t1)):
            ans.append([t1[i], 0])

    
print(len(ans))
for i in ans:
    print(i[0], i[1], sep='-')

