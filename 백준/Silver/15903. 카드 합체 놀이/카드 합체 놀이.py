import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

heapq.heapify(arr)  # 리스트를 heap으로 변환

for _ in range(m):
    first = heapq.heappop(arr)  # 가장 작은 수
    second = heapq.heappop(arr)  # 두 번째로 작은 수
    min = first + second  # 둘의 합

    heapq.heappush(arr, min)  # 두 개 다 바꿔 줘야 하기에
    heapq.heappush(arr, min)  # 두 번 넣기

print(sum(arr))  # 모든 수들의 합