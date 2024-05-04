days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(int(input())):
    l = list(input())
    y = ''.join(l[0:4])
    m = ''.join(l[4:6])
    d = ''.join(l[6:8])

    print(f'#{i+1} {y}/{m}/{d}' if 0 < int(m) < 13 and 0 < int(d) < days[int(m)-1]+1 else f'#{i+1} -1')