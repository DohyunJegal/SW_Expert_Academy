for T in range(int(input())):
    p, q = map(float, input().split())
    # 1번 뒤집는 경우(s1) > 잘못된 면으로 시작(1-p), 1번만 뒤집음(q)
    s1 = (1-p)*q
    # 2번 뒤집는 경우(s2) > 제대로 된 면으로 시작(p), 2번 뒤집음(q > 1-q)
    s2 = p*(1-q)*q
    print(f'#{T+1} YES' if s1<s2 else f'#{T+1} NO')