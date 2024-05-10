for T in range(int(input())):
    N = int(input())
    lst = [list(map(int, str(input().rstrip()))) for _ in range(N)]
    res, s, e = 0, N//2, N//2
    for i in range(N):
        res += sum(lst[i][s:e+1])
        if i >= N//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1
    print(f'#{T+1} {res}')