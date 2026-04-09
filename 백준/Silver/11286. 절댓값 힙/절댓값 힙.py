import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(str(heapq.heappop(heap)[1]) + '\n')
        else:
            print('0\n')