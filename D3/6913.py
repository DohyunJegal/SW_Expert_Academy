for T in range(int(input())):
    N, M = map(int, input().split())
    lst = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        lst.append(tmp.count(1))
    print(f'#{T+1} {lst.count(max(lst))} {max(lst)}')