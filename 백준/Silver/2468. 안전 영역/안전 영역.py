import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n  # x, y 값이 주어진 숫자보다 커지지 않게


def dfs(x, y, h):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = True  # 방문 표시

    for i in range(4):  # 상하좌우
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, n):  # 범위 안이라면
            if not visited[nx][ny] and island[nx][ny] > h:  # 방문하지 않았고 안전한 섬이라면
                dfs(nx, ny, h)  # 재귀적으로


n = int(input())

island = []
height = 0
safe = 0

for _ in range(n):
    row = list(map(int, input().split()))  # 각 줄 입력받기
    island.append(row)  # 리스트 추가
    height = max(height, max(row))  # 최댓값 찾아서 높이로

for h in range(height):
    visited = [[False] * n for _ in range(n)]  # n*n만큼 부울 초기화
    result = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and island[i][j] > h:  # 방문하지 않았고 안전한 섬이라면
                dfs(i, j, h)
                result += 1
    safe = max(safe, result)  # 안전한 섬들의 최댓값

print(safe)