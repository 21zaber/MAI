s = input()
n = len(s)

def check(l, r):
    if l == r:
        return True
    if l == r - 1:
        return s[l] == s[r]
    return s[l] == s[r] and check(l+1, r-1)

ans = 0

for i in range(n):
    for j in range(i, n):
        if j-i+1 > ans and check(i, j):
            ans = j - i + 1

print(ans)
