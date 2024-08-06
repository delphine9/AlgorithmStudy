import sys
from collections import deque  # deque 불러오기

input = sys.stdin.readline


def in_range(temp):
    return 0 <= temp <= 100000  # temp 값이 주어진 숫자보다 커지거나 작아지지 않게


def bfs(s):
    global cnt
    queue = deque([s])  # queue에 삽입
    visited[s] = True  # 방문 표시

    while queue:  # 큐가 비어있지 않으면
        for _ in range(len(queue)):  # 현재 큐의 길이만큼 반복
            temp = queue.popleft()  # 현재 위치
            if temp == k:  # 동생 위치 도착했다면
                return  # 바로 탈출
            for next in (temp+1, temp-1, temp*2):  # 다음으로 갈 수 있는 세 가지
                if in_range(next):  # 다음 위치가 범위 안이라면
                    if not visited[next]:  # 방문하지 않았다면
                        arr[next] = temp  # 현재 위치를 다음 위치 배열값으로
                        queue.append(next)  # 해당 노드를 큐에 추가
                        visited[next] = True  # 방문 표시

        cnt += 1


n, k = map(int, input().split())

visited = [False] * 100001  # 1000000+1만큼 부울 초기화
cnt = 0
arr = [0] * 100001  # 1000000+1민큼 0으로 채우기

bfs(n)
print(cnt)

path = []

while k != n:  # 역으로 도착할 때까지
    path.append(k)  # 현재 위치 삽입
    k = arr[k]  # 현재 위치가 담고 있는 예전 위치
path.append(n)  # 수빈 위치 삽입

print(' '.join(map(str, path[::-1])))  # 역순으로 출력