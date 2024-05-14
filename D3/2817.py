from itertools import combinations

for T in range(int(input())):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    count = 0
    for i in range(1, N+1):
        temp = combinations(lst, i)
        for j in temp:
            if sum(j) == K:
                count += 1
    print(f'#{T+1} {count}')