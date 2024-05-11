for _ in range(10):
    T = int(input())
    lst = [list(map(str, str(input().strip()))) for _ in range(100)]
    res = 0
    # 가로
    for i in range(100):
        for j in range(100):
            for k in range(100-j):
                if lst[i][j:j+k+1] == lst[i][j:j+k+1][::-1]:
                    res = max(res, len(lst[i][j:j+k+1]))
    # 세로
    for l in range(100):
        temp = []
        for m in range(100):
            temp.append(lst[m][l])
        for o in range(100):
            for p in range(100-o):
                if temp[o:o+p] == temp[o:o+p][::-1]:
                    res = max(res, len(temp[o:o+p]))
    print(f'#{T} {res}')