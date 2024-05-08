def func(a, b):
    if b > 0:
        return func(a, b-1) * a
    else:
        return 1

for _ in range(10):
    T = int(input())
    N, M = map(int, input().split())
    print(f'#{T} {func(N, M)}')