for T in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        A, B = B, A
        N, M = M, N

    res = 0
    for i in range(0, M-N+1):
        tmp = 0
        for j in range(0, N):
            tmp += A[j]*B[i+j]
        res = max(res, tmp)

    print(f'#{T+1} {res}')