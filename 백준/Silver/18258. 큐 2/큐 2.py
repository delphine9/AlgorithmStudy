import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write


class DQueue:
    def __init__(self):
        self.items = deque()

    def push(self, item):  # 아이템 삽입
        self.items.append(item)

    def pop(self):  # empty가 아니라면 출력, 이라면 -1
        if not self.empty():
            return self.items.popleft()
        return -1

    def size(self):  # 길이 재기
        return len(self.items)

    def empty(self):  # 길이가 0이라면 empty
        return len(self.items) == 0

    def front(self):  # 첫번째 아이템 출력
        if not self.empty():
            return self.items[0]
        return -1

    def back(self):  # 마지막 아이템 출력
        if not self.empty():
            return self.items[-1]
        return -1


dque = DQueue()
arr = []

n = int(input())
for i in range(n):  # n번 입력받기
    command = input().split()  # 띄어쓰기로 구분
    x = command[0]  # x는 명령어로

    if x == 'push':
        y = command[1]  # y는 아이템으로
        dque.push(y)

    elif x == 'pop':
        arr.append(str(dque.pop()))

    elif x == 'size':
        arr.append(str(dque.size()))

    elif x == 'empty':
        if dque.empty():  # empty라면
            arr.append("1")
        else:  # 아니라면
            arr.append("0")

    elif x == 'front':
        arr.append(str(dque.front()))

    elif x == 'back':
        arr.append(str(dque.back()))

print("\n".join(arr))  # 하나의 문자열로 한번에 출력