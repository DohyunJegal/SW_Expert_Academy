for T in range(10):
    N = int(input())
    orig = list(input().split())
    M = int(input())
    order = list(input().split())

    for i in range(len(order)):
        if order[i] == 'I':
            for j in range(int(order[i+2])):
                orig.insert(int(order[i+1])+j, order[i+3+j])
        elif order[i] == 'D':
            for k in range(int(order[i+2])):
                del orig[int(order[i+1])]
        elif order[i] == 'A':
            for l in range(int(order[i+1])):
                orig.append(order[i+2+l])

    print(f'#{T+1}', end=' ')
    for o in range(10):
        print(orig[o], end=' ')
    print()