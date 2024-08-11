n = int(input())

dp = [0] * 1001  # (n+1)까지

dp[1] = 1  # 2x1인 경우
dp[2] = 3  # 2x2인 경우

for i in range(3, n+1):  # 3부터 n까지
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-2]) % 10007  # n = (n-1) + (n-2) + (n-2)임

print(dp[n])