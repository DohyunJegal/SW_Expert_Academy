for T in range(10):
    N = int(input())
    orig = list(map(int, input().split()))
    c = int(input())
    order = list(map(str, input().split()))
    for i in range(len(order)):
        if order[i] == 'I':
            for j in range(int(order[i+2])):
                orig.insert(int(order[i+1])+j, order[i+3+j])
    print(f'#{T+1}', end=' ')
    for k in range(10):
        print(orig[k], end=' ')
    print()