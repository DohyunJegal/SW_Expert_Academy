for T in range(int(input())):
    s = input().rstrip()
    curr = [1, 1]
    for i in s:
        if i == 'L':
            curr = [curr[0], curr[0]+curr[1]]
        elif i == 'R':
            curr = [curr[0]+curr[1], curr[1]]
    print(f'#{T+1} {curr[0]} {curr[1]}')