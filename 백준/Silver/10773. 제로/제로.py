class Stack:
    def __init__(self):  # 스택 초기화
        self.items = []

    def push(self, item):  # 아이템 삽입
        self.items.append(item)

    def pop(self):  # 아이템 출력
        if not self.IsEmpty():
            return self.items.pop()
        return None

    def IsEmpty(self):  # 길이가 0이라면 empty
        return len(self.items) == 0

    def sum(self):
        return sum(self.items)


stk = Stack()

k = int(input())

for i in range(k):
    x = int(input())

    if x == 0:
        stk.pop()
    else:
        stk.push(x)

print(stk.sum())