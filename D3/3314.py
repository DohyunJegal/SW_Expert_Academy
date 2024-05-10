for T in range(int(input())):
    lst = map(int, input().split())
    new_lst = []
    for i in lst:
        if i <= 40:
            new_lst.append(40)
        else:
            new_lst.append(i)
    print(f'#{T+1} {sum(new_lst)//len(new_lst)}')
