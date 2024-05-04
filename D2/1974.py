f = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

for T in range(int(input())):
    case = []
    for _ in range(9):
        case.append(list(map(int, input().split())))

    res = 1

    for i in range(9):
        tmp = set([])
        for j in range(9):
            tmp.add(case[j][i])
        if tmp != f:
            res = 0

    for j in range(9):
        if set(case[j]) != f:
            res = 0

    tmp2 = set([])
    for k in range(0, 9, 3):
        for l in range(3):
            tmp2.update(case[k+l][k:k+3])
        if tmp2 != f:
            res = 0

    print(f'#{T+1} {res}')
