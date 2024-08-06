import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))  # 한줄에 입력받기

dp = [0] * (n + 1)  # dp 초기화

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + temp[i - 1]  # 누적 합 저장

maxTemp = -float('inf')  # 최솟값 지정

for i in range(k, n+1):  # k개 사이의 누적합을 알기 위해
    curTemp = dp[i] - dp[i-k]
    if curTemp > maxTemp:
        maxTemp = curTemp  # 최댓값이 나오면 갱신


print(maxTemp)