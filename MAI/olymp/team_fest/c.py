n, l, r = map(int, input().split())

l -= 1
r -= 1

if l % 2 == 0:
    ans =  '()' * (l // 2) 
   # print(1, ans)
    ans += '[]' * ((r-l+1) // 2) 
  #  print(2, ans)
    ans += '()' * ((n - r - 1) // 2)
 #   print(3, ans)
else:
    n -= 2
    l -= 1
    r -= 1
    ans = '()' * (l // 2) + '[]' * ((r-l+1) // 2) + '()' * ((n - r - 1) // 2) 
    ans = '(' + ans + ')'

print(ans)


