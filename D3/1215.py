for i in range(10):
    n = int(input())
    words = [list(map(str, str(input().rstrip()))) for _ in range(8)]
    cnt = 0
    # 가로
    for j in range(8):
        for k in range(0, 8-n+1):
            if words[j][k:k+n] == words[j][k:k+n][::-1]:
                cnt += 1
    # 세로
    temp = []
    for l in range(8):
        for m in range(0, 8-n+1):
            for o in range(0, n):
                temp.append(words[m+o][l])
            if temp == temp[::-1]:
                cnt += 1
            temp = []
    print(f'#{i+1} {cnt}')