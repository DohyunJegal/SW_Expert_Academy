d = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

for T in range(int(input())):
    m1, d1, m2, d2 = map(int, input().split())
    print(f'#{T+1} {(d[m2-1]+d2)-(d[m1-1]+d1)+1}')