for T in range(int(input())):
    N, D = map(int, input().split())
    D = D*2+1
    cnt = 0
    while D*cnt < N:
        cnt += 1
    print(f'#{T+1} {cnt}')