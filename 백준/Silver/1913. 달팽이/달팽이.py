def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n  # x, y 값이 주어진 숫자보다 커지지 않게


n = int(input())
m = int(input())
arr = [[0 for col in range(n)] for row in range(n)]  # 2차원 배열 생성

x, y, dirnum = 0, 0, 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]  # 남동북서 순서

arr[x][y] = n*n  # 시작점

for i in range(n*n-1, 0, -1):
    nx, ny = x + dx[dirnum], y + dy[dirnum]

    # 범위를 벗어나거나 이미 지나온길일때
    if not in_range(nx, ny, n) or arr[nx][ny] != 0:
        dirnum = (dirnum+1) % 4  # 남동북서 순서대로
        nx, ny = x + dx[dirnum], y + dy[dirnum]  # 새로운 위치

    x, y = nx, ny  # 새로운 값 할당
    arr[x][y] = i  # 현재 위치에 번호 할당

for row in arr:  # 행을 배열만큼
    for num in row:  # 정수를 행만큼
        print(num, end=" ")  # 정수 출력
    print()  # 한줄띄우기

for i in range(len(arr)):  # 배열길이만큼 반복
    if m in arr[i]:  # 행에 있다면
        print(i+1, arr[i].index(m)+1)  # 행+1, 행에서m을찾아서인덱스+1
        break  # 찾으면 탈출