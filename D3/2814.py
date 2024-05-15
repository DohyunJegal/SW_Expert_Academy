def dfs(node, depth):
    global res
    visited[node] = 1
    for n in lst[node]:
        if visited[n] == 0:
            dfs(n, depth+1)
    visited[node] = 0
    res = max(res, depth)

for T in range(int(input())):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    res = 0
    for _ in range(M):
        x, y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x)
    for i in range(N+1):
        dfs(i, 1)
    print(f'#{T+1} {res}')