for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    up, down = 0, 0
    for i in range(1, N):
        if lst[i-1]<lst[i]:
            up = max(up, lst[i]-lst[i-1])
        elif lst[i-1]>lst[i]:
            down = max(down, lst[i-1]-lst[i])
    print(f'#{T+1} {up} {down}')