import sys
from collections import deque  # deque 불러오기

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m  # x, y 값이 주어진 숫자보다 커지지 않게


def bfs(i, j):
    queue = deque([(i, j, 1)])  # queue에 시작점과 거리 삽입ㄴ

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[i][j] = True  # 방문 표시

    while queue:
        x, y, dis = queue.popleft()  # 현재 위치와 거리 출력

        if x == n-1 and y == m-1:  # 도착점에 도달하면
            return dis

        for i in range(4):  # 상하좌우
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny, n, m):  # 범위 안이라면
                if not visited[nx][ny] and maze[nx][ny] == 1:  # 방문하지 않았고 갈 수 있는 길이라면
                    queue.append((nx, ny, dis + 1))  # 해당 위치와 거리를 큐에 추가
                    visited[nx][ny] = True  # 방문 표시

    return -1


n, m = map(int, input().split())

maze = []
visited = [[False] * m for _ in range(n)]  # n*m만큼 부울 초기화

for _ in range(n):
    row = list(map(int, input().strip()))  # 각 줄 정수리스트로 입력받기
    maze.append(row)  # 리스트 추가


result = bfs(0, 0)

print(result)