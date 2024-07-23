import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(h):
    global cnt  # 전역함수
    visited[h] = True  # 방문 표시
    arr[h] = cnt  # 방문 순서
    cnt += 1  # 다음 순서
    graph[h].sort(reverse=True)  # 내림차순 정렬 -> 큰 순서부터
    for e in graph[h]:  # 연결되어 있는 것만큼
        if not visited[e]:  # 방문하지 않았다면
            dfs(e)  # 재귀적으로 수행


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

dfs(r)

for i in range(1, n+1):
    print(arr[i])