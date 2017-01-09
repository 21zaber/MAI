t = list(map(int, input().split()))

class Node:
    l = -1
    r = -1
    v = 0
    par = 0
    size = 0

tree = Node()
cur = tree

for i in range(len(t)):
    cur.v = t[i]
    if t[i+1] < cur.v:
        n = Node()
        cur.l = n
        n.par = cur
        cur = n
        continue
    

    

