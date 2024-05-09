for T in range(10):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        temp = ''
        for j in range(n):
            if case[j][i] != 0:
                temp += str(case[j][i])
        res += temp.count('12')
    print(f'#{T+1} {res}')