for T in range(int(input())):
    K = int(input())
    lst = list(map(int, input().split()))
    res = 0
    while len(lst)>=2:
        temp = []
        for i in range(0, len(lst), 2):
            res += abs(lst[i]-lst[i+1])
            temp.append(max(lst[i], lst[i+1]))
        lst = temp
    print(f'#{T+1} {res}')