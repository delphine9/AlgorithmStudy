import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
dic = {}

for _ in range(n):
    name, log = map(str, input().split())
    if log == "enter":
        dic[name] = log
    else:
        del dic[name]

print("\n".join(sorted(dic.keys(), reverse=True)) + "\n") # 사전순의 역순