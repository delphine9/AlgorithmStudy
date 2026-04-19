import sys
import math

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

for i in range(n):
    n, m = map(int, input().split())

    cnt = math.comb(m, n)

    print(str(cnt) + '\n')