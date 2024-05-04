for T in range(int(input())):
    n = int(input())
    lst = sorted(list(map(int, input().split())), reverse=True)
    cnt = {}
    for i in lst:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    print(f'#{n} {cnt[0][0]}')