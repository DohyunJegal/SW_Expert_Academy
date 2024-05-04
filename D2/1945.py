nums = [11, 7, 5, 3, 2]

for T in range(int(input())):
    N = int(input())
    res = []
    for i in nums:
        tmp = N
        count = 0
        while tmp % i == 0:
            tmp //= i
            count += 1
        res.insert(0, count)

    print(f'#{T+1}', end=' ')
    print(*res)