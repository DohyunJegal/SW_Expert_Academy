password = ['1011000', '1001100', '1100100', '1011110', '1100010', '1000110', '1111010', '1101110', '1110110', '1101000']

for T in range(int(input())):
    N, M = map(int, input().split())
    res = 0
    for i in range(N):
        t = input().rstrip()
        if int(t) != 0:
            t = str(int(t[::-1]))
            lst = []
            for j in range(0, 50, 7):
                lst.append(password.index(t[j:j+7]))
            res = sum(lst) if ((lst[1]+lst[3]+lst[5]+lst[7])*3+lst[0]+lst[2]+lst[4]+lst[6])%10 == 0 else 0
    print(f'#{T+1} {res}')