for T in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{T+1} {sum(lst) + N + max(lst)}')