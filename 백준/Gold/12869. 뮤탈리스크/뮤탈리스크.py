n = int(input())
scv = list(map(int, input().split())) + \
    [0] * (3-n)  # 3보다 작은 걸 대비하여 나머지 0으로 채우기

attack = [[-9, -3, -1], [-9, -1, -3], [-1, -3, -9],
          [-1, -9, -3], [-3, -9, -1], [-3, -1, -9]]  # 가능한 경우 6가지

arr = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]

minCount = float("inf")


def dfs(scv1, scv2, scv3, count):

    global minCount

    if (scv1 == 0 and scv2 == 0 and scv3 == 0):  # 체력이 모두 0이 되었을 때
        minCount = min(count, minCount)  # 최솟값 갱신
        return

    if (minCount <= count):  # 현재의 횟수가 현재의 최솟값보다 커지면 탈출
        return

    # 방문했던 건데 횟수가 현재의 횟수보다 작거나 같으면 탈출
    if (arr[scv1][scv2][scv3] != 0 and arr[scv1][scv2][scv3] <= count):
        return

    arr[scv1][scv2][scv3] = count  # 각각의 배열에 횟수 저장

    for i in range(6):  # 가능한 경우가 6개
        newscv1 = max(scv1+attack[i][0], 0)  # 첫 번째 경우부터
        newscv2 = max(scv2+attack[i][1], 0)
        newscv3 = max(scv3+attack[i][2], 0)  # 마지막 경우까지
        dfs(newscv1, newscv2, newscv3, count+1)  # 횟수 1씩 추가하기


dfs(scv[0], scv[1], scv[2], 0)

print(minCount)