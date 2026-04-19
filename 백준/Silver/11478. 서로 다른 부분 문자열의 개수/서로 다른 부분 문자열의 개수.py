import sys

input = sys.stdin.readline
print = sys.stdout.write

s = str(input().strip())

result = set() # 중복 제거를 위해 set 사용

for i in range(len(s)):
    for j in range(i, len(s)):
        result.add(s[i:j+1])

print(str(len(result)))