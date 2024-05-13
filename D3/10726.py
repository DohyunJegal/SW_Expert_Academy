for T in range(int(input())):
    N, M = map(int, input().split())
    M = format(M, 'b').zfill(N)[::-1]
    cnt = 0
    for i in range(N):
        if M[i] == '1':
            cnt += 1
    print(f'#{T+1} ON' if cnt == N else f'#{T+1} OFF')