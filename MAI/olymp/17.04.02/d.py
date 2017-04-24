s = input()


m = [0 for i in s]
h = [0 for i in s]

for i in range(len(s)):
    if i == 0:
        if s[i] == 'M':
            m[0] = 1
        elif s[i] == 'H':
            h[0] = 1
    else:
        h[i] = h[i-1]
        m[i] = m[i-1]
        if s[i] == 'M':
            m[i] += 1
        elif s[i] == 'H':
            h[i] += 1
        else:
            if h[i] < 1:
                m[i] = 0
                h[i] = 0
            else:
                h[i] -= 1


print(max(m))


