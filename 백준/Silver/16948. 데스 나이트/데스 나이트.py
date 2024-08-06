import sys
from collections import deque  # deque 불러오기

input = sys.stdin.readline


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n  # x, y 값이 주어진 숫자보다 커지지 않게


def bfs(i, j):
    queue = deque([(i, j, 0)])  # queue에 시작점과 거리 삽입

    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    visited[i][j] = True  # 방문 표시

    while queue:
        x, y, dis = queue.popleft()  # 현재 위치와 거리 출력

        if x == r2 and y == c2:  # 도착점에 도달하면
            return dis

        for i in range(6):  # 여섯방향
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny, n):  # 범위 안이라면
                if not visited[nx][ny]:  # 방문하지 않았다면
                    queue.append((nx, ny, dis + 1))  # 해당 위치와 거리를 큐에 추가
                    visited[nx][ny] = True  # 방문 표시

    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [[False] * n for _ in range(n)]  # n*m만큼 부울 초기화

result = bfs(r1, c1)

print(result)