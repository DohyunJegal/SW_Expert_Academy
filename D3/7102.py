for T in range(int(input())):
    N, M = map(int, input().split())
    lst = {}
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i+j not in lst:
                lst[i+j] = 1
            else:
                lst[i+j] += 1

    lst = dict(sorted(lst.items()))
    lst = dict(sorted(lst.items(), key=lambda x: x[1], reverse=True))

    print(f'#{T+1}', end=' ')
    print(*[k for k, v in lst.items() if v == max(lst.values())])