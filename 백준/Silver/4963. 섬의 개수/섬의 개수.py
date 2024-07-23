import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def in_range(x, y, h, w):
    return 0 <= x < h and 0 <= y < w  # x, y 값이 주어진 숫자보다 커지지 않게


def dfs(x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    visited[x][y] = True  # 방문 표시

    for i in range(8):  # 상하좌우대각선
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, h, w):  # 범위 안이라면
            if not visited[nx][ny] and island[nx][ny] == 1:  # 방문하지 않은 섬이라면
                dfs(nx, ny)  # 재귀적으로


results = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break  # 0 0 받으면 탈출

    island = []
    visited = [[False] * w for _ in range(h)]  # w*h만큼 부울 초기화
    result = 0  # 0에서 시작

    for _ in range(h):  # h번
        island.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and island[i][j] == 1:  # 방문하지 않은 섬이라면
                dfs(i, j)
                result += 1

    results.append(result)

for i in results:
    print(i)  # 한 번에 출력