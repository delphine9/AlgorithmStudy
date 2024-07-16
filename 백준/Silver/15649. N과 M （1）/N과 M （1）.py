def pprint():
    # arrayList를 문자열로 받아 result 배열에 공백을 두고 넣기
    result.append(' '.join(map(str, arrayList)))


def dfs(h):
    if h == m:  # m이라면
        pprint()  # pprint함수
        return

    for i in range(1, n+1):  # 1부터 n번 반복
        if visited[i]:  # True면 중복이라 건너뛰기
            continue

        arrayList.append(i)  # i 넣고
        visited[i] = True  # 중복 방지로 True
        dfs(h+1)  # 1씩 추가해주다가
        arrayList.pop()  # m이 되면 pop
        visited[i] = False  # pop했으니까 False


n, m = map(int, input().split())
arrayList = []  # 넣었다 빼고 반복할 배열
result = []  # 최종 결과물을 담은 배열
visited = [False] * (n+1)


dfs(0)
print('\n'.join(result))  # 결과 한번에 출력