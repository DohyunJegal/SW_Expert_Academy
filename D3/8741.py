for T in range(int(input())):
    lst = list(input().split())
    print(f'#{T+1}', end=' ')
    for i in lst:
        print(str.upper(i[0]), end='')
    print()