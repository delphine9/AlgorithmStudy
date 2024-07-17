def pprint():
    # arrayList를 문자열로 받아 result 배열에 공백을 두고 넣기
    result.append(' '.join(map(str, arrayList)))


def dfs(v, h):
    if h == m:  # m이라면
        pprint()  # pprint함수
        return

    for i in range(1, n+1):  # 1부터 n까지 반복
        arrayList.append(array2[i-1])  # 1부터 시작했기에 i-1 넣고
        dfs(i+1, h+1)  # 1씩 추가해주다가
        arrayList.pop()  # m이 되면 pop


n, m = map(int, input().split())
array = list(map(int, input().split()))  # list로 받기
array2 = sorted(array)  # 받은 리스트 오름차순 정렬
arrayList = []  # 넣었다 빼고 반복할 배열
result = []  # 최종 결과물을 담은 배열
visited = [False] * n  # visited 초기화


dfs(1, 0)
print('\n'.join(result))  # 결과 한번에 출력