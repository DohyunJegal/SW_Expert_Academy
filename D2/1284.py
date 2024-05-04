for T in range(int(input())):
    # A사 : 1리터당 P원, B사 : 기본 요금 Q, 기본 R리터 초과 시 1리터당 S원, 종민이가 사용한 물 W리터
    P, Q, R, S, W = map(int, input().split())
    A = P*W
    B = Q+(S*(W-R)) if W > R else Q
    print(f'#{T+1} {min(A, B)}')