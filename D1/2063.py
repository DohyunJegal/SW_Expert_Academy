n = int(input())
lst = list(map(int, input().split()))
print(sorted(lst)[n//2])