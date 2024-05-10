for T in range(int(input())):
    n = int(input())*2
    print(f'#{T+1} {n//60%12} {n%60}')