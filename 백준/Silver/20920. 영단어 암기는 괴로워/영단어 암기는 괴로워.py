import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
word_map = {}

for i in range(n):
    words = input().strip()
    if len(words) >= m:
        if words in word_map:
            word_map[words] += 1
        else:
            word_map[words] = 1
sorted_word_map = sorted(word_map.items(), key = lambda x: (-x[1], -len(x[0]), x[0])) # 단어의 빈도수, 길이, 사전순으로 정렬
print('\n'.join(map(lambda x: x[0], sorted_word_map)))