for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    max_price, res, cnt = 0, 0, 0
    for i in range(N-1, -1, -1):
        if lst[i] > max_price:
            max_price = lst[i]
            res += cnt
            cnt = 0
        else:
            cnt += max_price - lst[i]
    res += cnt
    print(f'#{T+1} {res}')