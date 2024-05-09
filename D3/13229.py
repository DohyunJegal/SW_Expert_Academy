d = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}

for T in range(int(input())):
    print(f'#{T+1} {d[input().rstrip()]}')