n = int(input())

if n < 4:
    print(-1)
    exit()

t = ['4', '2', '3', '1']

for i in range(5, n+1):
    t.append(str(i))

print(' '.join(t))
