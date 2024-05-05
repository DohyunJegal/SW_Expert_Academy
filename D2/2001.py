for T in range(int(input())):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += flies[i+k][j+l]
            res = max(res, tmp)
    print(f'#{T+1} {res}')