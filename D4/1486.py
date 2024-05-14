from itertools import *

for T in range(int(input())):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    res = []
    for i in range(1, N+1):
        for j in list(combinations(lst, i)):
            if sum(list(j)) >= B:
                res.append(sum(list(j))-B)
    print(f'#{T+1} {min(res)}')