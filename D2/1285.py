# 1285. 아름이의 돌 던지기 >> c++만 제출가능!

for T in range(int(input())):
    N = int(input())
    lst = list(map(abs, map(int, input().split())))
    print(f'#{T+1} {min(lst)} {lst.count(min(lst))}')