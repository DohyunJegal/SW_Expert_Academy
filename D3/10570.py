for T in range(int(input())):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        tmp = list(map(str, str(i)))
        tmp2 = list(map(str, str(int(i**0.5)))) if i**0.5 == int(i**0.5) else list(map(str, str(i**0.5)))
        if tmp == tmp[::-1] and tmp2 == tmp2[::-1]:
            cnt += 1
    print(f'#{T+1} {cnt}')