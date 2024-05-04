for i in range(int(input())):
    a, b = map(int, input().split())
    print(f'#{i+1}', end=' ')
    if a>b: print('>')
    elif a==b: print('=')
    else: print('<')