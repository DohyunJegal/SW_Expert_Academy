m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for T in range(int(input())):
    N = int(input())
    res = []
    for i in m:
        res.append(N//i)
        N %= i
    print(f'#{T+1}')
    print(*res)