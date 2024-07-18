import sys

input = sys.stdin.readline


def dfs(h, cur_i, cur_j, cur_sum):
    global max_sum  # 전역함수
    if h == k:  # k개만큼 선택했으면
        max_sum = max(cur_sum, max_sum)  # max 함수로 비교 후 더 큰 값
        return

    for i in range(cur_i, n):  # 현재 i부터 n까지 반복
        # i가 cur_i와 같으면 cur_j부터 아니면 0부터, m까지 반복
        for j in range(cur_j if i == cur_i else 0, m):
            if not visited[i][j]:  # 아직 방문되지 않았으면
                # 선택한 칸이 다른 칸과 인접하지 않으면
                if (i == 0 or not visited[i-1][j]) and (i == n-1 or not visited[i+1][j]) and (j == 0 or not visited[i][j-1]) and (j == m-1 or not visited[i][j+1]):
                    result.append(array[i][j])  # 배열에 넣어준다
                    visited[i][j] = True  # 선택한 뒤
                    dfs(h+1, i, j+1, cur_sum+array[i][j])  # 1씩 더해주다가
                    result.pop()  # k가 되면 pop
                    visited[i][j] = False  # 선택 취소


n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]  # 배열생성
visited = [[False for _ in range(m)] for _ in range(n)]  # 배열크기만큼 초기화
result = []

max_sum = float("-inf")  # 가장 작은 음수값으로 초기화

dfs(0, 0, 0, 0)
print(max_sum)