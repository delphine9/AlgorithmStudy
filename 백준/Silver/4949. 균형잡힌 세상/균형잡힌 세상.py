import sys

input = sys.stdin.readline


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


def BalancedWorld(line):
    stk = Stack()
    for char in line:  # 문자열만큼
        if char == '.':  # 문장의 끝
            break
        if char in '([':  # 문자가 '([' 이라면
            stk.push(char)  # 문자 삽입
        elif char in ')]':  # 문자가 ')]'이라면
            if stk.IsEmpty():  # 앞에 '('가 없다면
                return False
            top = stk.pop()  # 맨위 출력
            # 대괄호와 소괄호 짝이 맞는지 확인
            if (char == ')' and top != '(') or (char == ']' and top != '['):
                return False
    return stk.IsEmpty()  # 비었다면 제대로 균형이 잡힌 것이고 (가 남아있다면 균형이 잡히지 않은 것


arr = []

while True:
    line = input().rstrip('\n')  # 오른쪽 끝만 제거
    if line == '.':  # .이 나오면 탈출
        break

    if all(char in ' .' for char in line):
        arr.append('yes')
    else:
        if BalancedWorld(line):  # True라면
            arr.append("yes")
        else:  # False라면
            arr.append("no")

print("\n".join(arr))  # 하나의 문자열로 한번에 출력