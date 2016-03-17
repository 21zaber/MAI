s = input()
n = int(input())
l = len(s)
direction = 1
b = 0

for i in range(n):
    q = int(input())
    b += direction * q
    direction *= -1
    b += direction
    b %= l

if direction == -1:
    b = l - b - 1
    s = s[::-1]

b %= l
print(s[b:] + s[:b])
