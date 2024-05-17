for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    res = [0]
    for i in range(N):
        for j in range(len(res)):
            res.append(lst[i]+res[j])
        res = list(set(res))
    print(f'#{T+1} {len(res)}')