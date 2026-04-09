import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

deq = deque(range(1, n+1))

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(str(deq[0]))