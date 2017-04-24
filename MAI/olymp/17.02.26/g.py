
n = int(input())

for i in range(n):
    m = int(input())
    s = input()
    c = list(map(int, input().split()))

    j = 0
    while s[j] == ")":
        j += 1
    s = s[j:]
    c = c[j:]
    j = -1
    while s[j] == "(":
        j -= 1
    if j < -1:
        s = s[:j+1]
        c = c[:j+1]

    oc, cc = 0, 0 
    for i in s:
        if i == '(':
            oc += 1
        else:
            cc += 1

    if oc > cc:
        s = s[::-1]
        t = ''
        for i in range(len(s)):
            if s[i] == '(':
                t += ')'
            else:
                t += '('
        s = t

    print(s)
    b = 0
    for i in range(len(s)):
        if s[i] == '(':
            b += 1
        else:
            b -= 1
        print(b, end=' ')


    
    
