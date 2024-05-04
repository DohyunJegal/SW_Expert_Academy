score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for T in range(int(input())):
    N, K = map(int, input().split())
    total = []
    s_total = []
    for i in range(N):
        m, f, a = map(int, input().split())
        total.append(m*0.35 + f*0.45 + a*0.20)
    s_total = sorted(total, reverse=True)
    print(f'#{T+1} {score[s_total.index(total[K-1])//(N//10)]}')