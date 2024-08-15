n = int(input())
Mt = []

for i in range(n):
    s, e = map(int, input().split())
    Mt.append((s, e))

Mt.sort(key=lambda Mt: Mt[0])  # 선 시작 시간을 기준으로 정렬
Mt.sort(key=lambda Mt: Mt[1])  # 후 종료 시간을 기준으로 정렬

time = []
time.append(Mt[0])  # 첫 번째 강의는 무조건
k = 0

for i in range(1, n):  # 첫번째 수업은 이미 넣었기에 1부터
    if Mt[i][0] >= Mt[k][1]:  # 시작 시간이 종료 시간보다 크거나 같으면
        time.append(Mt[i])
        k = i

print(len(time))