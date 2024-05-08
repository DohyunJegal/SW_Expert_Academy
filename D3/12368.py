for T in range(int(input())):
    A, B = map(int, input().split())
    print(f'#{T+1} {(A+B)%24}')