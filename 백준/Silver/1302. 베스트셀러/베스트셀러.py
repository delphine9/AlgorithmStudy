import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
d = dict()

for _ in range(n):
    name = str(input())
    if name in d:
        d[name] += 1
    else:
        d[name] = 1

m = max(d.values())
best = [k for k, v in d.items() if v == m] #최빈값이 여러개일 경우, 사전순으로 가장 앞서는 것을 출력하기 위해 리스트로 저장
best.sort()
print(best[0])