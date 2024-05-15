def checker(n):
    tmp = str(n)
    for a in range(len(tmp)-1):
        if tmp[a] > tmp[a+1]:
            return False
    return True

for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    res = -1
    for i in range(N-1):
        for j in range(i+1, N):
            t = lst[i]*lst[j]
            if checker(t):
                res = max(res, t)
    print(f'#{T+1} {res}')