t = int(input())

def msum(l):
    ans = 0
    for i in l:
        ans += a[i-1]
    return ans

for q in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    #a.sort(reverse = True)
    st = []
    for i in range(len(a)):
        id = -1
        for j in range(len(st)):
            if msum(st[j]) + a[i] <= s:
               #print('=================')
               #print("sum:", msum(st[j]) + a[i])
               #print(st[j])
               #print(a[i])
               #print('=================')
                id = j
                break
        if id == -1:
            st.append([i + 1])
        else:
            st[id].append(i + 1)
    #print(a)               
    print(len(st))
    for i in st:
        print(len(i), ' '.join(list(map(str, i))))


                

