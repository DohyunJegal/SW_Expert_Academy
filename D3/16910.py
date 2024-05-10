for T in range(int(input())):
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i**2 + j**2 <= N**2:
                count += 1
    print(f'#{T+1} {count*4 + N*4 + 1}')