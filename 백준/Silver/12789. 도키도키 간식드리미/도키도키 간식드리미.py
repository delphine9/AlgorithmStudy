import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
arr = list(map(int, input().split()))

stk = []
num = 1

for n in arr:
    if n == num:
        num += 1

        while stk and stk[-1] == num:
            stk.pop()
            num += 1
    else:
        stk.append(n)

if stk:
    print("Sad\n")
else:
    print("Nice\n")