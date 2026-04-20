import sys

input = sys.stdin.readline
print = sys.stdout.write

s = input().strip()
lst = list(map(int, s))
max_length = 0

for i in range(len(s)):
    for j in range(i+1, len(s), 2):
        mid = i + (j-i+1)//2 # 중간 지점 계산
        if sum(lst[i:mid])== sum(lst[mid:j+1]):
            max_length = max(max_length, j-i+1)
        else:
            continue

print(str(max_length))