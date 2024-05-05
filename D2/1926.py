N = int(input())
for i in range(1, N+1):
    t = str(i)
    if '3' in t or '6' in t or '9' in t:
        print('-'*(t.count('3')+t.count('6')+t.count('9')), end=' ')
    else:
        print(i, end=' ')