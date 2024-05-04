for i in range(int(input())):
    lst = list(map(int, input().split()))
    print(f'#{i+1} {max(lst)}')