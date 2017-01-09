n = int(input())

from math import sqrt

def isprime(a):
    if a > 2 and a % 2 == 0:
        return False
    for i in range(3, int(sqrt(a)) + 1, 2):
        if a % i == 0:
            return False

    return True

def isultra(a):
    s = str(a)
    if len(s) < 2:
        return True
    for i in range(1, len(s)):
        head = int(s[:i])
        tail = int(s[i:])
        if not(head in primes and tail in ultras):
            return False
    return True

t = 0
k = 2
primes = []
ultras = set()

while len(primes) < n:
    if isprime(k):
        primes.append(k)
    k += 1

primes = set(primes)

for i in primes:
    if isultra(i):
        ultras.add(i)

print(ultras)
print(len(ultras))

