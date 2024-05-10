for T in range(10):
    N, lst = input().split()
    res = []
    for i in lst:
        if res and i == res[-1]:
            res.pop()
        else:
            res.append(i)
    print(f'#{T+1}', end=' ')
    for j in res:
        print(j, end='')
    print()