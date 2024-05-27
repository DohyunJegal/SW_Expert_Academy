from collections import deque

def bfs(x, y):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for a in direction:
            nx, ny = x+a[0], y+a[1]
            if 0 <= nx < N and 0 <= ny < N and cnt[x][y]+lst[nx][ny] < cnt[nx][ny]:
                cnt[nx][ny] = cnt[x][y]+lst[nx][ny]
                queue.append((nx, ny))

for T in range(int(input())):
    N = int(input())
    lst = [list(map(int, input().strip())) for _ in range(N)]
    cnt = [[1e9]*N for _ in range(N)]
    cnt[0][0] = 0
    bfs(0, 0)
    print(f'#{T+1} {cnt[-1][-1]}')