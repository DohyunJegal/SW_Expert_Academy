a, b = map(int, input().split())
if a == 1:
    print('A' if b == 3 else 'B')
elif a == 2:
    print('A' if b == 1 else 'B')
else:
    print('A' if b == 2 else 'B')