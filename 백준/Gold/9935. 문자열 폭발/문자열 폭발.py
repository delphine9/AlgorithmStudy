import sys

input = sys.stdin.readline
print = sys.stdout.write

lst = list(input().strip()) #문자열을 한글자씩 리스트로 저장
bomb = list(input().strip())
stk = []

for i in range(len(lst)):
    stk.append(lst[i])
    if stk[-len(bomb):] == bomb:
        del stk[-len(bomb):]

if stk == []:
    print('FRULA')
else:
    print(''.join(stk))