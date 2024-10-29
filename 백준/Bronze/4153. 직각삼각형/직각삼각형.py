import sys

input = sys.stdin.readline

result = []

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if a**2 == (b**2+c**2):
        result.append("right")
    elif b**2 == (a**2+c**2):
        result.append("right")
    elif c**2 == (a**2+b**2):
        result.append("right")
    else:
        result.append("wrong")

for i in result:
    print(i)