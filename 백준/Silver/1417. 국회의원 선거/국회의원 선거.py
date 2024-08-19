import heapq

n = int(input())
arr = []

for i in range(n):
    arr.extend(list(map(int, input().split())))

dasom = arr[0]  # 다솜이는 기호 1번
arr = arr[1:]  # 1번 없애기

maxheap = []

for i in arr:
    heapq.heappush(maxheap, -i)  # 최대힙으로 변환

count = 0

# maxheap이 비어있는지 아닌지 확인한 후 다솜이가 최대값이 될때까지
while maxheap and dasom <= -maxheap[0]:
    max = -heapq.heappop(maxheap)  # 가장 큰 수
    dasom += 1  # 다솜이 한표 추가
    heapq.heappush(maxheap, -(max-1))  # 한 표 없어지고 삽입
    count += 1  # 횟수 증가

print(count)