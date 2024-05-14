def dfs(index, sm):
    global res
    if index == N:
        if sm == K:
            res += 1
        return
    # 다음 노드 선택 o
    dfs(index+1, sm+lst[index])
    # 다음 노드 선택 x
    dfs(index+1, sm)

for T in range(int(input())):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    res = 0
    dfs(0, 0)
    print(f'#{T+1} {res}')