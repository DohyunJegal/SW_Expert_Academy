for T in range(int(input())):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    res = []
    for i in range(1, N+1):
        if i not in lst:
            res.append(i)
    print(f'#{T+1}', end=' ')
    print(*sorted(res))