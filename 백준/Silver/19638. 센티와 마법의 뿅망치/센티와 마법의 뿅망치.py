import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

n, ch, t = map(int, input().split())
arr = []
cnt = 0

for _ in range(n):
    h = int(input())
    arr.append(-h) # 최대 힙을 구현하기 위해 음수로 저장
heapq.heapify(arr) # 리스트를 힙으로 변환

for _ in range(t):
    largest = -heapq.heappop(arr) # 다시 양수로 바꾸기

    if largest < ch or largest == 1: # 가장 큰 수가 ch보다 작거나 1이면 더 이상 줄일 수 없음
        heapq.heappush(arr, -largest)
        break
    else:
        heapq.heappush(arr, -(largest // 2)) # 절반으로 줄여서 다시 넣기
        cnt += 1
    
if -arr[0] >= ch:
    print("NO" + "\n")
    print(str(-arr[0]) + "\n")
else:
    print("YES" + "\n")
    print(str(cnt) + "\n")