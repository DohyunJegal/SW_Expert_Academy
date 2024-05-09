for T in range(int(input())):
    lst = map(int, input().split())
    res = []
    for i in lst:
        res.append(sum(list(map(int, str(i)))))
    print(f'#{T+1} {max(res)} {min(res)}')