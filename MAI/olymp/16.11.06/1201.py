c = 0
for i in range(6):
    if input() == 'W':
        c += 1

if c > 4:
    print(1)
    exit()
if c > 2:
    print(2)
    exit()
if c > 0:
    print(3)
    exit()
print(-1)

