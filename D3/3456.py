for T in range(int(input())):
    lst = map(int, input().split())
    res = {}
    for i in lst:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    print(f'#{T+1}', end=' ')
    print(*[k for k,v in res.items() if v == min(res.values())])