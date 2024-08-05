import sys
from collections import deque  # deque 불러오기

input = sys.stdin.readline


def bfs(h):
    global cnt  # 전역함수
    queue = deque([h])  # queue에 삽입
    visited[h] = True  # 방문 표시
    arr[h] = cnt  # 방문 순서
    cnt += 1  # 다음 순서

    while queue:
        temp = queue.popleft()  # 현재 노드
        for e in graph[temp]:  # 연결되어 있는 것만큼
            if not visited[e]:  # 방문하지 않았다면
                queue.append(e)  # 해당 노드를 큐에 추가
                visited[e] = True  # 방문 표시
                arr[e] = cnt  # 방문 순서 지정
                cnt += 1  # 다음 순서


n, m, r = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]  # 인접리스트 초기화
visited = [False] * (n+1)  # n+1만큼 부울 초기화
arr = [0] * (n+1)  # n+1민큼 0으로 채우기
cnt = 1  # 순서는 1번부터

for _ in range(m):  # 간선 개수만큼
    u, v = map(int, input().split())
    graph[u].append(v)  # 양쪽에
    graph[v].append(u)  # 넣어주기

for i in range(1, n+1):
    graph[i].sort()  # 오름차순 정렬

bfs(r)

for i in range(1, n+1):
    print(arr[i])