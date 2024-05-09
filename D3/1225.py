from collections import deque

for T in range(10):
    n = int(input())
    lst = deque(map(int, input().split()))
    flag = 0
    while flag != 1:
        for i in range(1, 6):
            tmp = lst.popleft()
            if tmp-i <= 0:
                lst.append(0)
                flag = 1
                break
            else:
                lst.append(tmp-i)
    print(f'#{T+1}', end=' ')
    print(*lst)