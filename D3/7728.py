for T in range(int(input())):
    X = list(map(str, str(int(input()))))
    res = {}
    for i in X:
        if i not in res:
            res[i] = 1
    print(f'#{T+1} {len(res)}')