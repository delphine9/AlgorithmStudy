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

    def IsEmpty(self):  # 길이가 0이라면 empty
        return len(self.items) == 0


arr = []
n = int(input())

for i in range(n):  # n번 입력받기
    stk = Stack()
    s = input().strip()
    correct = True

    for char in s:  # s의 문자열 동안
        if char == '(':  # 문자가 '('이라면
            stk.push(char)  # 삽입
        elif char == ')':  # 문자가 ')'이라면
            if stk.IsEmpty():  # 비어 있다면
                correct = False  # 잘못된 문자열
                break
            stk.pop()  # 비어 있지 않다면 맨위 출력
    if not stk.IsEmpty():  # 마지막에 비어 있지 않다면
        correct = False  # 잘못된 문자열

    arr.append("YES" if correct else "NO")  # 참이면 YES 아니면 NO

print("\n".join(arr))  # 하나의 문자열로 한번에 출력