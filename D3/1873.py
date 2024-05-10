for T in range(int(input())):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    order = input().rstrip()
    current = [0, 0]

    # 현재 위치 확인
    for i in range(H):
        for j in range(W):
            tmp = field[i][j]
            if tmp == '^' or tmp == 'v' or tmp == '<' or tmp == '>':
                current = [i, j]

    # 명령 수행
    for k in order:
        if k == 'U':
            field[current[0]][current[1]] = '^'
            if current[0]-1 >= 0 and field[current[0]-1][current[1]] == '.':
                field[current[0]-1][current[1]] = '^'
                field[current[0]][current[1]] = '.'
                current[0] -= 1
        elif k == 'D':
            field[current[0]][current[1]] = 'v'
            if current[0]+1 < H and field[current[0]+1][current[1]] == '.':
                field[current[0]+1][current[1]] = 'v'
                field[current[0]][current[1]] = '.'
                current[0] += 1
        elif k == 'L':
            field[current[0]][current[1]] = '<'
            if current[1]-1 >= 0 and field[current[0]][current[1]-1] == '.':
                field[current[0]][current[1]-1] = '<'
                field[current[0]][current[1]] = '.'
                current[1] -= 1
        elif k == 'R':
            field[current[0]][current[1]] = '>'
            if current[1]+1 < W and field[current[0]][current[1]+1] == '.':
                field[current[0]][current[1]+1] = '>'
                field[current[0]][current[1]] = '.'
                current[1] += 1
        elif k == 'S':
            if field[current[0]][current[1]] == '^':
                for l in range(current[0], -1, -1):
                    if field[l][current[1]] == '*':
                        field[l][current[1]] = '.'
                        break
                    elif field[l][current[1]] == '#':
                        break
            elif field[current[0]][current[1]] == 'v':
                for m in range(current[0], H, 1):
                    if field[m][current[1]] == '*':
                        field[m][current[1]] = '.'
                        break
                    elif field[m][current[1]] == '#':
                        break
            elif field[current[0]][current[1]] == '<':
                for o in range(current[1], -1, -1):
                    if field[current[0]][o] == '*':
                        field[current[0]][o] = '.'
                        break
                    elif field[current[0]][o] == '#':
                        break
            elif field[current[0]][current[1]] == '>':
                for p in range(current[1], W, 1):
                    if field[current[0]][p] == '*':
                        field[current[0]][p] = '.'
                        break
                    elif field[current[0]][p] == '#':
                        break

    print(f'#{T + 1}', end=' ')
    for q in range(len(field)):
        for r in range(len(field[q])):
            print(field[q][r], end='')
        print()