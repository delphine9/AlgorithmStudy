import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

lst = []

for i in range(9):
    lst.append(int(input()))

for i in combinations(lst, 7):
    if sum(i) == 100:
        print('\n'.join(map(str, sorted(i))))
        break