for T in range(int(input())):
    s = input().rstrip()
    t = {}
    r = ''
    for i in s:
        if i in t:
            t[i] += 1
        else:
            t[i] = 1
    t = sorted(t.items())
    for j in t:
        if j[1]%2 != 0:
            r += j[0]
    print(f'#{T+1}', end=' ')
    print(r if r != '' else 'Good')