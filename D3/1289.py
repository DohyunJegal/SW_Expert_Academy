for T in range(int(input())):
    orig = input().rstrip()
    checker, cnt = 0, 0
    for i in orig:
        if int(i) != checker:
            cnt += 1
            checker = int(i)
    print(f'#{T+1} {cnt}')