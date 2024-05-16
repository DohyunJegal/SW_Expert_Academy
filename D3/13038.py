def cnt(index, goal):
    global res
    days = 0
    while goal > 0:
        if lst[index%7] == 1:
            goal -= 1
        days += 1
        index += 1
    res = min(res, days)

for T in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    res = 1e9
    for i in range(len(lst)):
        cnt(i, n)
    print(f'#{T+1} {res}')