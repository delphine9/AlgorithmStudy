import heapq

n = int(input())

arr = []

for _ in range(n):
    line = list(map(int, input().split()))
    for i in line:
        if len(arr) == n:
            if arr[0] < i:  # 가장 작은 수보다 크면
                heapq.heappop(arr)  # 가장 작은 수 제거
                heapq.heappush(arr, i)  # 새로운 수 삽입
        else:
            heapq.heappush(arr, i)

print(heapq.heappop(arr))  # n번째 큰 수