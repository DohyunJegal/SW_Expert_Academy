order = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

for T in range(int(input())):
    a, n = map(str, input().split())
    lst = list(map(str, input().split()))
    cnt = [0]*10
    for i in range(10):
        cnt[i] = lst.count(order[i])
    print(cnt)
    print(f'#{T+1}')
    for j in range(10):
        print((order[j]+' ')*cnt[j], end='')