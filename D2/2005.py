for T in range(int(input())):
    N = int(input())
    res = [[]]
    for i in range(1, N+1):
        tmp = []
        for j in range(1, i+1):
            if j==1 or j==i:
                tmp.append(1)
            else:
                tmp.append(res[i-1][j-2]+res[i-1][j-1])
        res.append(tmp)
    print(f'#{T+1}')
    for k in res[1:]:
        print(*k)