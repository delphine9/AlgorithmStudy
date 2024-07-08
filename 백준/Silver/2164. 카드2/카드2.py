from collections import deque  # deque 불러오기


class DQueue:
    def __init__(self):
        self.items = deque()

    def push(self, item):  # 아이템 삽입
        self.items.append(item)

    def pop(self):  # empty가 아니라면 출력, 이라면 -1
        if not self.empty():
            return self.items.popleft()
        return -1

    def empty(self):  # 길이가 0이라면 empty
        return len(self.items) == 0


dque = DQueue()
arr = []

n = int(input())
card = int()

for i in range(1, n+1):  # n번만큼 반복
    dque.push(i)  # i까지 넣기

while (dque):  # 비어있지 않을때까지
    card = dque.pop()  # 맨앞 출력
    if (dque.empty()):  # 비었다면 탈출
        break
    card = dque.pop()  # 맨앞 출력
    dque.push(card)  # 맨뒤로 삽입

print(card)