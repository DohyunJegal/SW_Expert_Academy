for T in range(10):
    dump = int(input())
    lst = sorted(list(map(int, input().split())))
    for i in range(dump):
        if max(lst)-min(lst) == 1:
            break
        lst[-1] -= 1
        lst[0] += 1
        lst.sort()
    print(f'#{T+1} {max(lst)-min(lst)}')
