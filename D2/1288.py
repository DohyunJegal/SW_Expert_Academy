f = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for T in range(int(input())):
    N = int(input())
    lst = set(list(map(int, str(N))))

    c = 0
    while f != lst:
        c += 1
        lst.update(set(list(map(int, str(c*N)))))

    print(f'#{T+1} {c*N}')