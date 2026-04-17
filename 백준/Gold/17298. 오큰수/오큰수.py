import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
lst = list(map(int, input().split()))

ans = [-1] * n
stack = []

for i in range(n):
    while stack and lst[stack[-1]] < lst[i]: # 스택이 비어있지 않고, 현재 수가 스택의 마지막 인덱스에 해당하는 수보다 크면
        ans[stack.pop()] = lst[i]
    stack.append(i)

print(' '.join(map(str, ans)))