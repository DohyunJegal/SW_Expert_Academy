for T in range(int(input())):
    n = int(input())
    print(f'#{T+1}', end=' ')
    print('Alice' if n%2==0 else 'Bob')