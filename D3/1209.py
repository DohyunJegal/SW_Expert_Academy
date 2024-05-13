for T in range(10):
    n = int(input())
    # 0~99 == 가로, 100~199 == 세로, 200 == LR, 201 == RL
    res = [0]*202
    for i in range(100):
        lst = list(map(int, input().split()))
        res[i] = sum(lst)
        for j in range(100):
            res[100+j] += lst[j]
        res[200] += lst[i]
        res[201] += lst[100-i-1]
    print(f'#{n} {max(res)}')