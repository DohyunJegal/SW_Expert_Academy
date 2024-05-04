for T in range(int(input())):
    total = 0
    tmp = 0
    for N in range(int(input())):
        a = input()
        if int(a[0]) == 1:
            tmp += int(a[2])
        elif int(a[0]) == 2:
            if 0 < tmp - int(a[2]):
                tmp -= int(a[2])
            else:
                tmp = 0
        total += tmp
    print(f'#{T+1} {total}')