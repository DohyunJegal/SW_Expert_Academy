for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    avg = sum(lst)/len(lst)
    cnt = 0
    for i in lst:
        if i <= avg:
            cnt += 1
    print(f'#{T+1} {cnt}')