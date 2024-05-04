for T in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())
    mt = (h1*60+m1) + (h2*60+m2)
    h = mt//60
    m = mt%60
    if h > 12:
        h -= 12
    print(f'#{T+1} {h} {m}')