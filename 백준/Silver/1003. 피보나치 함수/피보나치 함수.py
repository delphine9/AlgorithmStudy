import sys
input = sys.stdin.readline


def fibonacci(n):
    if (n == 0):
        return 1, 0
    elif (n == 1):
        return 0, 1

    fibo = [(1, 0), (0, 1)]
    for i in range(2, n+1):
        fibo.append((fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1] + fibo[i-2][1]))

    return fibo[n]


n = int(input())
result = []

for _ in range(n):
    num = int(input())
    cnt0, cnt1 = fibonacci(num)
    result.append(str(cnt0) + " " + str(cnt1))

print('\n'.join(result))