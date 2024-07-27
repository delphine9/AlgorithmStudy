import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n  # x, y 값이 주어진 숫자보다 커지지 않게


def dfs(x, y):
    global aparts
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = True  # 방문 표시
    aparts += 1  # 단지 내 아파트 개수 하나씩 추가

    for i in range(4):  # 상하좌우
        nx, ny = x + dx[i], y + dy[i]
        if in_range(nx, ny, n):  # 범위 안이라면
            if not visited[nx][ny] and apart[nx][ny] == 1:  # 방문하지 않은 아파트라면
                dfs(nx, ny)  # 재귀적으로


n = int(input())

apart = []
visited = [[False] * n for _ in range(n)]  # n*n만큼 부울 초기화
apartlist = []

for _ in range(n):
    apart.append(list(map(int, input().strip())))  # 띄어쓰기 없이 각 줄 입력받기

for i in range(n):
    for j in range(n):
        if not visited[i][j] and apart[i][j] == 1:  # 방문하지 않은 아파트라면
            aparts = 0  # 다른 아파트기에 초기화
            dfs(i, j)
            apartlist.append(aparts)  # 아파트 개수 추가

print(len(apartlist))  # 아파트단지 개수
for i in sorted(apartlist):  # 오름차순으로 정렬
    print(i)