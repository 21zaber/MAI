t = [2, 3, 37, 5, 7, 73, 53, 373, 23]
t.sort()

n = int(input())
if n > 9:
    print(-1)
else:    
    print(t[n-1])

