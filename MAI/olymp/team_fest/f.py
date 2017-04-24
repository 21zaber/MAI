n = int(input())

pos = None
start = None
light = None
end = 0

for i in range(n):
    x, r = map(int, input().split())

    end = x
    if pos is None:
        pos = x
        start = x
        light = x

    if pos < x-r:
        continue

    if x > light:
        print(-1)
        exit(0)

    light = max(light, x+r)
    pos = x

if pos != end:
    print(-1)
else:
    print(3 * abs(end - start))

    

    
