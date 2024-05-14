o = {'o..': 0, '.o.': 1, '..o': 2}

for t in range(int(input())):
    s, n = input().split()
    s = o[s]
    for i in range(int(n)):
        if s == 0:
            s = 1
        elif s == 1:
            s = 0
        elif s == 2:
            s = 1
    print(f'#{t+1} {s}')