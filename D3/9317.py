for T in range(int(input())):
    N = int(input())
    ans = input().rstrip()
    inp = input().rstrip()
    cnt = 0
    for i in range(N):
        if ans[i] == inp[i]:
            cnt += 1
    print(f'#{T+1} {cnt}')