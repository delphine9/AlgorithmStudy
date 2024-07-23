import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m  # x, y 값이 주어진 숫자보다 커지지 않게


def dfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = True  # 방문 표시

    for i in range(4):  # 상하좌우
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, n, m):  # 범위 안이라면
            if not visited[nx][ny] and arr[nx][ny] == 1:  # 방문하지 않은 배추라면
                dfs(nx, ny)  # 재귀적으로


t = int(input())
results = []

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]  # m만큼 부울 초기화
    result = 0  # 0에서 시작

    for _ in range(k):  # k번
        x, y = map(int, input().split())
        arr[y][x] = 1  # 배추 1로 설정해 주기

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:  # 방문하지 않은 배추라면
                dfs(i, j)
                result += 1

    results.append(result)

for i in results:
    print(i)