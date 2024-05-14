for T in range(int(input())):
    # n = 개수, l = 제한
    n, l = map(int, input().split())

    # t = 가치, k = 무게
    lst = [[0, 0]]
    for _ in range(n):
        t, k = map(int, input().split())
        lst.append([t, k])
    d = [[0]*(l+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, l+1):
            if j < lst[i][1]:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j], d[i-1][j-lst[i][1]]+lst[i][0])

    print(f'#{T+1} {d[n][l]}')