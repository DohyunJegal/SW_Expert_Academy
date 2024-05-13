for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    d = [1]*N
    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            if lst[i] > lst[j]:
                d[i] = max(d[i], d[j]+1)
    print(f'#{T+1} {max(d)}')