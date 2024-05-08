for T in range(int(input())):
    L, U, X = map(int, input().split())
    print(f'#{T+1}', end=' ')
    if X>=L and X<=U:
        print(0)
    elif X<L:
        print(L-X)
    else:
        print(-1)