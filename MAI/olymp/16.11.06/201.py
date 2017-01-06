n, m, k = map(int, input().split())

t = []

a = [100000, -100000]

for i in range(k):
    t.append(list(map(int, input().split())))
    if t[-1][0] < a[0]:
        a = t[-1][:]
    elif t[-1][0] == a[0] and t[-1][1] > a[1]:
        a = t[-1][:]

for i in t:
    if i[0] < a[0] and i[1] < a[1]:
        print("Impossible")#Impossible
        exit()

t.sort(key=(lambda x: x[0] * 10000 + x[1]))
t.append([n, m])

pos = [1, 1]
for i in t:
    if i[0] != pos[0]:
        print('D'*(i[0]-pos[0]), end="")
        pos[0] = i[0]
    if i[1] != pos[1]:
        print('R'*(i[1]-pos[1]), end="")
        pos[1] = i[1]

print()

    
