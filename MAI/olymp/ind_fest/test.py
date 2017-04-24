
print(1717 + 239)

exit(0)

s = 0

with open("input001.txt", "r") as f:
    s += sum(list(map(int, ' '.join(f.readlines()).split() )))

with open("output001.txt", "r") as f:
    s += sum(list(map(int, ' '.join(f.readlines()).split() )))

print(s)

exit(0)

n = 10 ** 3

t = 1
for i in range(n):
    for j in range(n):
        t *= i
        if t > 1000000000:
            t = 1

print(t)
