m = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

down = abs(a[0] + [0, m][a[0] < b[0]] - b[0])
up = abs(a[0] - [0, m][a[0] > b[0]] - b[0]) 

#print(down, up)
if (a[1] - down) % m == b[1]:
    print(min(up, down))
else:
    print(-1)
