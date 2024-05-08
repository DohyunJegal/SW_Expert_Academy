vowels = ['a', 'e', 'i', 'o', 'u']

for T in range(int(input())):
    orig = input().rstrip()
    res = ''
    for i in orig:
        if i not in vowels:
            res += i
    print(f'#{T+1} {res}')