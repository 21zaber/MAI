n = int(input())

def ans(f):
    if f == 'A':
        print('Bananenfrau')
    else:
        print('Apfelmann')

def swp(a):
    if a == 'A':
        return 'B'
    else:
        return 'A'

for i in range(n):
    s = input()
    count = {'A': s.count('A'), 'B': s.count('B')}
    l, r = s.split('C')
    l = l[::-1]

    if l and r and l[-1] == r[-1]:
        ans(l[-1])
        continue

    player = 'A'
    lp, rp = 0, 0
    ll, rl = len(l), len(r)

    while count['A'] > 0 and count['B'] > 0:
        if lp < ll and rp < rl and l[lp] == player and r[rp] == player:
            if l[-1] == player:
                lp += 1
            else:
                rp += 1
            count[player] -= 1
        elif lp < ll and l[lp] == player:
            lp += 1
            count[player] -= 1
        elif rp < rl and r[rp] == player:
            rp += 1
            count[player] -= 1
        
        if count[player] <= 0:
            ans(swp(player))
            break

        player = swp(player)
