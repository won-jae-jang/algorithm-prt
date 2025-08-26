N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: (-x[1])) #과제물 점수가 높은 순으로
result = 0
process = [False] * (1001) # i일에 과제를 수행했는가
for d, score in data:
    #현재 과제물을 수행할 수 있는 경우
    for date in range(d, 0, -1):
        if not process[date]:
            process[date] = True
            result += score
            break

print(result)