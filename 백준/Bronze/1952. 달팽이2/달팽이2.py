def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m  # x, y 값이 주어진 숫자보다 커지지 않게


m, n = input().split()
m, n = int(m), int(n)
arr = [[0 for col in range(n)] for row in range(m)]  # 2차원 배열 생성

x, y, dirnum = 0, 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # 동남서북 순서

arr[x][y] = 1  # 시작점

turn = 0  # 방향 전환 횟수

for i in range(2, n*m+1):
    nx, ny = x + dx[dirnum], y + dy[dirnum]

    # 범위를 벗어나거나 이미 지나온길일때
    if not in_range(nx, ny, m, n) or arr[nx][ny] != 0:
        dirnum = (dirnum+1) % 4  # 동남서북 순서대로
        nx, ny = x + dx[dirnum], y + dy[dirnum]  # 새로운 위치
        turn += 1  # 꺾었으니까 +1

    x, y = nx, ny  # 새로운 값 할당
    arr[x][y] = i  # 현재 위치에 번호 할당

print(turn)