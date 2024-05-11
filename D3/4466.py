for T in range(int(input())):
    N, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())), reverse=True)
    res = 0
    for i in range(K):
        res += lst[i]
    print(f'#{T+1} {res}')