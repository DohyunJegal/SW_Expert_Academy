for T in range(int(input())):
    N, A, B = map(int, input().split())
    res = 1e9
    for R in range(1, N+1):
        C = 1
        while R*C <= N:
            res = min(res, A*abs(R-C)+B*(N-R*C))
            C += 1
    print(f'#{T+1} {res}')