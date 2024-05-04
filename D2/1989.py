for T in range(int(input())):
    word = list(str(input()))
    backword = word[::-1]
    print(f'#{T+1}', end=' ')
    print('1' if word == backword else '0')