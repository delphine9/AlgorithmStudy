import sys

input = sys.stdin.readline


def dfs(k):
    global cnt  # 전역변수

    if k == n:  # n개만큼 선택되었으면
        cnt += 1
        return

    for i in range(n):
        # 같은 열, 우상향 대각선, 좌상향 대각선 범위 모두 퀸이 없을 때
        if not down[i] and not y_x[k+i] and not y__x[(n-1)+k-i]:
            down[i] = True  # 표시
            y_x[k+i] = True  # 표시
            y__x[(n-1)+k-i] = True  # 표시
            dfs(k+1)
            down[i] = False  # 표시 해제
            y_x[k+i] = False  # 표시 해제
            y__x[(n-1)+k-i] = False  # 표시 해제


n = int(input())
map = [[0]*n for _ in range(n)]  # 배열크기만큼 초기화
down = [False] * n  # 같은 열 범위
y_x = [False] * (2*(n-1)+1)  # 우상향 대각선 범위
y__x = [False] * (2*(n-1)+1)  # 좌상향 대각선 범위

cnt = 0

dfs(0)
print(cnt)