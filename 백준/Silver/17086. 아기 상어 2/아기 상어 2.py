import sys
from collections import deque  # deque 불러오기

input = sys.stdin.readline


def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m  # x, y 값이 주어진 숫자보다 커지지 않게


def bfs(i, j):
    queue = deque([(i, j, 0)])  # queue에 시작점과 거리 삽입

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    visited = [[False] * m for _ in range(n)]  # 매번 n*m만큼 부울 초기화해 줘야 함
    visited[i][j] = True  # 방문 표시

    while queue:
        x, y, dis = queue.popleft()  # 현재 위치와 거리 출력

        if shark[x][y] == 1:  # 상어 만나면
            return dis  # 거리 출력

        for i in range(8):  # 상하좌우대각선
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny, n, m):  # 범위 안이라면
                if not visited[nx][ny]:  # 방문하지 않았다면
                    queue.append((nx, ny, dis + 1))  # 해당 위치와 거리를 큐에 추가
                    visited[nx][ny] = True  # 방문 표시

    return -1


n, m = map(int, input().strip().split())

shark = []
maxSafe = 0

for _ in range(n):
    row = list(map(int, input().strip().split()))  # 각 줄 정수리스트로 입력받기
    shark.append(row)  # 리스트 추가

for i in range(n):
    for j in range(m):
        if shark[i][j] == 0:  # 빈칸이라면
            safe = bfs(i, j)
            maxSafe = max(safe, maxSafe)  # 최댓값 갱신

print(maxSafe)