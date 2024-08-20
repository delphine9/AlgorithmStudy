import sys
import heapq

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]  # 인접리스트 초기화

for _ in range(m):  # 간선 개수만큼
    u, v = map(int, input().split())
    graph[u].append((v, 1))  # 도로의 거리는 1

dis = [float('inf')] * (n+1)  # 가장 큰 값으로 초기화
dis[x] = 0  # 출발점은 거리가 0

heap = []
heapq.heappush(heap, (0, x))  # 거리와 도시

while heap:
    curdis, curcity = heapq.heappop(heap)

    if dis[curcity] < curdis:  # 이미 더 짧은 거리가 있다면
        continue
    for nextcity, weight in graph[curcity]:  # 인접 도시 확인
        newdis = curdis + weight  # 현재 거리에 지금 갈 거리

        if newdis < dis[nextcity]:  # 새로운 거리가 원래 거리보다 짧다면
            dis[nextcity] = newdis  # 새로운 거리로 갱신
            heapq.heappush(heap, (newdis, nextcity))

result = []

for i in range(1, n+1):
    if dis[i] == k:  # 거리가 k라면
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)