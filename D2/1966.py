for T in range(int(input())):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    print(f'#{T+1}', end=' ')
    print(*lst)