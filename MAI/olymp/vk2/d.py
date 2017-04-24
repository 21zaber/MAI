n = int(input())
s = input()

def parse(s, i=0):
    ss = i
    start = i
    h = 0
    while i < len(s) and s[i] == '[':
        i, nh = parse(s, i+1)
        h = max(h, nh+2)
        #print(s[start:i], h)
        start = i

    #print("parse {}:{} {}".format(start, i+1, h))
    if i == ss:
        h = 1
    return i+1, h

_, h = parse(s)

l = 4 * n
mid = (h-1) // 2
buf = [[' ' for i in range(l)] for i in range(h)]

def draw(s, h, i=0, p=0):
    if i >= len(s):
        return
    if s[i] == '[':
        r = (h-1)//2
        for j in range(r):
            buf[mid+j][p] = '|'
            buf[mid-j][p] = '|'
        buf[mid+r][p] = '+'
        buf[mid-r][p] = '+'
        buf[mid+r][p+1] = '-'
        buf[mid-r][p+1] = '-'
        draw(s, h-2, i+1, p+1)
    else:
        h += 2
        if s[i-1] == '[':
            p += 3
        r = (h-1)//2
        for j in range(r):
            buf[mid+j][p] = '|'
            buf[mid-j][p] = '|'
        buf[mid+r][p] = '+'
        buf[mid-r][p] = '+'
        buf[mid+r][p-1] = '-'
        buf[mid-r][p-1] = '-'
        draw(s, h, i+1, p+1)
        
        

draw(s, h)
for i in range(h):
    l = -1
    for j in range(len(buf[i])):
        if buf[i][j] != ' ':
            l = j+1
    buf[i] = buf[i][:l]

for i in buf:
    print(''.join(i))


