n = int(input())

dp = [[0]*10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1  # 한자리 숫자의 경우

for i in range(2, n+1):  # i자리 계단수
    for j in range(10):  # j로 끝나는 숫자
        if (j == 0):
            dp[i][j] = dp[i-1][1]  # 0일때는 1만 가능
        elif (j == 9):
            dp[i][j] = dp[i-1][8]  # 9일때는 8만 가능
        else:
            # 뒷자리수 앞에 올 수 있는 경우의 수 두가지의 합
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = (sum(dp[n]) % 1000000000)
print(result)