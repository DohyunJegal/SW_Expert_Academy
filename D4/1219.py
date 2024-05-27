def dfs(node):
    global res
    if node == 99:
        res = 1
        return
    for a in lst[node]:
        dfs(a)

for _ in range(10):
    res = 0
    T, N = map(int, input().split())
    lst = [[] for _ in range(100)]
    tmp = list(map(int, input().split()))
    for i in range(0, N*2, 2):
        lst[tmp[i]].append(tmp[i+1])
    dfs(0)
    print(f'#{T} {res}')