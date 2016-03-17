def factor(a):
    if a == 1:
        return {}
    end = int(a ** 0.5) + 1
    ans = {}
    for i in range(2, end):
        while a % i == 0:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
            a //= i
    if a > 1:
        ans[a] = 1
    return ans

def c(f, t, k):
    i = 0
    ans = 1
    while i < k and i <= t - f:
        ans *= f + i
        ans //= i + 1
        i += 1
    while i <= t - f:
        ans *= f + i
        i += 1

    while i < k:
        ans //= i + 1
        i += 1
    return ans
    
def c1(f, t, k):
    ans = 1
    print(f, t, k)
    for i in range(f, t+1):
        ans *= i

    for i in range(2, k+1):
        ans //= i

    return ans


k = int(input())
d, m = map(int, input().split())
mod = 10 ** 9 + 9

t = d ** (k-1)
if m % t != 0 :
    print(0)
    exit()

m = m // t

q = factor(m)
#print(q)

keys = q.keys()

ans = 1

for i in keys:
    a = q[i]
 #   print("fact: ", c(a + 1, a + k - 1, k - 1))
    ans = (ans * c(a +1, a + k - 1, k - 1)) % mod

print(ans)

    


