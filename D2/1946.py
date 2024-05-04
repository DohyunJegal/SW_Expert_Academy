for T in range(int(input())):
    orig = ''
    for N in range(int(input())):
        i = input().split()
        orig += i[0]*int(i[1])

    print(f'#{T+1}')
    for j in range(0, len(orig), 10):
        print(orig[j:j+10])