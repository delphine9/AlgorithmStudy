import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
numCards = set(map(int, input().split())) # 리스트 대신 집합을 사용하여 탐색 속도를 O(1)로 줄임
m = int(input())
MyNums = list(map(int, input().split()))

for num in MyNums:
    if num in numCards:
        print("1 ")
    else:
        print("0 ")