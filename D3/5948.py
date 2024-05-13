for T in range(int(input())):
    lst = list(map(int, input().split()))
    res = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i]+lst[j]+lst[k] not in res:
                    res.append(lst[i]+lst[j]+lst[k])
    print(f'#{T+1} {sorted(res, reverse=True)[4]}')