import sys
from collections import deque  # deque 불러오기

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
queue = deque(range(1, n+1))  # 1~n까지

result = []
while queue:  # 큐가 빌 때까지
    for _ in range(k-1):  # k까지
        queue.append(queue.popleft())  # k번째 전까지는 pop해서 뒤쪽에 넣기
    result.append(str(queue.popleft()))  # k번째는 pop해서 result에 넣기

print("<" + ", ".join(result) + ">")