for T in range(int(input())):
    s = input().rstrip()
    c = 1
    while s[0:c] != s[c:(c*2)]:
        c += 1
    print(f'#{T+1} {c}')