n = int(input())
place = list(map(int, input().split()))

start = 0
result = 0

sum = [place[0]] #누적합 리스트
for i in range(1, n):
    sum.append(sum[i - 1] + place[i])

# 통발이 가장 오른쪽에 있는 경우 -> i는 상대적으로 오른쪽에 있는 벌의 위치
for i in range(1, n - 1):
    left = sum[n - 1] - place[0] - place[i]
    right = sum[n - 1] - sum[i]
    result = max(result, left + right)

# 통발이 가장 왼쪽에 있는 경우 -> i는 상대적으로 왼쪽에 있는 벌의 위치
for i in range(1, n - 1):
    left = sum[i - 1]
    right = sum[n - 2] - place[i]
    result = max(result, left + right)

#통발이 꿀벌 사이에 있는 경우 -> 꿀벌은 각각 왼쪽, 오른쪽 끝에 위치
for i in range(1, n - 1):
    result = max(result, sum[n - 1] + place[i] - place[0] - place[n - 1])

print(result)