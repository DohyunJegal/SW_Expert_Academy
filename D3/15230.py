alphabet = 'abcdefghijklmnopqrstuvwxyz'

for T in range(int(input())):
    lst = input().rstrip()
    res = 0
    for i in range(len(lst)):
        if lst[i] == alphabet[i]:
            res += 1
        else:
            break
    print(f'#{T+1} {res}')