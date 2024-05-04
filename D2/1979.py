for T in range(int(input())):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    res = []

    cnt = 0
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(puzzle[j][i])
        for k in range(N):
            if tmp[k] == 1:
                cnt += 1
            elif tmp[k] == 0:
                if cnt != 0:
                    res.append(cnt)
                    cnt = 0
        if cnt != 0:
            res.append(cnt)
            cnt = 0

    cnt2 = 0
    for k in range(N):
        for l in range(N):
            if puzzle[k][l] == 1:
                cnt2 += 1
            elif puzzle[k][l] == 0:
                if cnt2 != 0:
                    res.append(cnt2)
                    cnt2 = 0
        if cnt2 != 0:
            res.append(cnt2)
            cnt2 = 0

    print(f'#{T+1} {res.count(K)}')
