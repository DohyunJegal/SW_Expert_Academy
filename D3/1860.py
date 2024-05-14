for T in range(int(input())):
    N, M, K = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    bread, cnt, res = 0, 0, 'Possible'
    for i in range(lst[-1]+1):
        if i//M != 0 and i%M == 0:
            bread += K
        if i == lst[cnt]:
            if bread != 0:
                bread -= 1
                cnt += 1
            else:
                res = 'Impossible'
                break
    print(f'#{T+1} {res}')