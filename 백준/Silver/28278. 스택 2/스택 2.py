import sys

input = sys.stdin.readline
print = sys.stdout.write


class Stack:
    def __init__(self):  # 스택 초기화
        self.items = []

    def push(self, item):  # 아이템 삽입
        self.items.append(item)

    def pop(self):  # empty가 아니라면 출력, 이라면 -1
        if not self.IsEmpty():
            return self.items.pop()
        return -1

    def peek(self):  # empty가 아니라면 맨위 출력, 이라면 -1
        if not self.IsEmpty():
            return self.items[-1]
        return -1

    def IsEmpty(self):  # 길이가 0이라면 empty
        return len(self.items) == 0

    def How(self):  # 길이 재기
        return len(self.items)


stk = Stack()
arr = []

n = int(input())

for i in range(n):  # n번 입력받기
    command = list(map(int, input().split()))  # 띄어쓰기로 구분하여 정수형으로 받는다
    x = command[0]  # x는 명령어로

    if x == 1:
        y = command[1]  # y는 아이템으로
        stk.push(y)

    elif x == 2:
        arr.append(str(stk.pop()))

    elif x == 3:
        arr.append(str(stk.How()))

    elif x == 4:
        if stk.IsEmpty():  # empty라면
            arr.append("1")
        else:  # 아니라면
            arr.append("0")

    elif x == 5:
        arr.append(str(stk.peek()))

print("\n".join(arr))  # 하나의 문자열로 한번에 출력