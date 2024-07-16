n, m = map(int, input().split())
arrayList = []
result = []


def pprint():
    result.append(' '.join(map(str, arrayList)))


def dfs(h):
    if h == m:
        pprint()
        return

    for i in range(1, n+1):
        arrayList.append(i)
        dfs(h+1)
        arrayList.pop()


dfs(0)
print('\n'.join(result))