def dfs(x, y, depth, s):
    if depth == 7:
        res.append(s)
        return
    s += str(lst[x][y])
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for a in direction:
        if 0<=x+a[0]<4 and 0<=y+a[1]<4:
            dfs(x+a[0], y+a[1], depth+1, s)

for T in range(int(input())):
    lst = [list(map(int, input().split())) for _ in range(4)]
    res = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')
    print(f'#{T+1} {len(set(res))}')