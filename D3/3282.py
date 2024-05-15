for T in range(int(input())):
    # N = 개수, K = 제한
    N, K = map(int, input().split())
    d = [[0]*(K+1) for _ in range(N+1)]
    lst = [[0, 0]]
    for _ in range(N):
        # V = 부피, C = 가치
        V, C = map(int, input().split())
        lst.append([V, C])
    for i in range(1, N+1):
        for j in range(1, K+1):
            if j<lst[i][0]:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j-lst[i][0]]+lst[i][1], d[i-1][j])
    print(f'#{T+1} {d[N][K]}')