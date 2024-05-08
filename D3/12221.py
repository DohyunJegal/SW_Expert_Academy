for T in range(int(input())):
    A, B = map(int, input().split())
    print(f'#{T+1} {A*B}' if 0<A<10 and 0<B<10 else f'#{T+1} -1')