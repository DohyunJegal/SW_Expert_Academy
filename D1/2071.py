for T in range(int(input())):
    lst = list(map(int, input().split()))
    print(f'#{T+1} {round(sum(lst)/len(lst))}')