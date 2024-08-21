import sys
import heapq

input = sys.stdin.readline

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]  # 인접리스트 초기화

for i in range(d):
    graph[i].append((i+1, 1))  # 직선 경로

for _ in range(n):  # 지름길의 개수만큼
    u, v, r = map(int, input().split())
    if v <= d:  # 도착 위치가 d보다 작으면
        graph[u].append((v, r))  # 도착 위치와 지름길의 길이

dis = [float('inf')] * (d+1)  # 가장 큰 값으로 초기화
dis[0] = 0  # 시작점의 거리는 0

heap = []
heapq.heappush(heap, (0, 0))  # 거리와 시작점

while heap:
    curdis, start = heapq.heappop(heap)

    if dis[start] < curdis:
        continue
    for end, weight in graph[start]:
        newdis = curdis + weight  # 현재 거리에 지금 갈 거리

        if newdis < dis[end]:  # 새로운 거리가 원래 거리보다 짧다면
            dis[end] = newdis  # 새로운 거리로 갱신
            heapq.heappush(heap, (newdis, end))

print(dis[d])  # 도착지의 최솟값