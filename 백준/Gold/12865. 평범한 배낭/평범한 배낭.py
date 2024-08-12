n, k = map(int, input().split())

bp = []
dp = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    w, v = map(int, input().split())
    bp.append((w, v))

for i in range(1, n+1):
    w, v = bp[i-1]
    for j in range(k+1):  # 최대 무게까지
        if j < w:  # 현재 배낭의 무게보다 최대 무게가 작으면
            dp[i][j] = dp[i-1][j]  # 배낭에 넣지 않았기에 이전 값 그대로
        else:
            # 현재 배낭을 넣지 않았을 때와 넣었을 때의 최댓값 
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[n][k])