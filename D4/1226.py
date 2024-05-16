def dfs(x, y):
    global res
    move = [[1, 0],[0, 1],[-1, 0],[0, -1]]
    for a in move:
        if lst[x+a[0]][y+a[1]] == 3:
            res = 1
            return
        elif lst[x+a[0]][y+a[1]] == 0:
            lst[x][y] = 1
            dfs(x+a[0], y+a[1])
            lst[x][y] = 0

for _ in range(10):
    T = int(input())
    lst = [list(map(int, str(input().strip()))) for _ in range(16)]
    res = 0
    dfs(1, 1)
    print(f'#{T} {res}')