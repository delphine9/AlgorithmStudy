import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n, l = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque()

for i in range(n):
    while dq and dq[-1][0] > arr[i]: # 현재 값보다 큰 값 제거
        dq.pop()

    dq.append((arr[i], i)) # 현재 값과 인덱스 저장
    
    if dq[0][1] < i-l+1: # 이전 인덱스면(범위 외) 제거
        dq.popleft()

    print(str(dq[0][0]) + " ")