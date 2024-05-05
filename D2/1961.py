def rotate(m, n):
    t = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(n-1, -1, -1):
            t[i][n-j-1] = m[j][i]
    return t

for T in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    mat_90 = rotate(matrix, N)
    mat_180 = rotate(mat_90, N)
    mat_270 = rotate(mat_180, N)

    print(f'#{T+1}')
    for i in range(N):
        print(''.join(map(str, mat_90[i])), end=' ')
        print(''.join(map(str, mat_180[i])), end=' ')
        print(''.join(map(str, mat_270[i])), end='\n')