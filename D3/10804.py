for T in range(int(input())):
    s = input().rstrip()
    r = []
    for i in s[::-1]:
        if i == 'b':
            r.append('d')
        elif i == 'd':
            r.append('b')
        elif i == 'p':
            r.append('q')
        elif i == 'q':
            r.append('p')
    print(f'#{T+1}', end=' ')
    for j in r:
        print(j, end='')
    print()