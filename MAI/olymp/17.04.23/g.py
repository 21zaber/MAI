s = input()

l = 0
r = 0

for i in s:
    if i == 'R':
        break
    l += 1

for i in s[::-1]:
    if i == 'L':
        break
    r += 1

#if l == 0:
#    l = 1
#if r == 0:
#    r = 1

print(min(r + l + 1, len(s)))


