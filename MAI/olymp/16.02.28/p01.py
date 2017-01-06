n = int(input())

def checkq(t):
    return (t[0] > t[3]) or (t[0] == t[3] and t[1] > t[4]) or (t[0] == t[3] and t[1] == t[4] and t[2] > t[5])

def checkc(t):
    return sum(t[:3]) > sum(t[3:])


for i in range(n):
    t = list(map(int, input().split()))
    q = checkq(t)
    c = checkc(t)
    if q and c:
        print("Win")
        continue
    if q:
        print("Quality")
        continue
    if c:
        print("Count")
        continue
    print("None")

