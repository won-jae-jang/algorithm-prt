n = int(input())
data = []
max_value = 0
for i in range(n):
    a, b = map(int, input().split())
    max_value = max(max_value, b)
    data.append((b - a, a, b)) #회의 소요시간, 시작 시간, 끝나는 시간

data.sort()
# print(data)

#Todo 종료조건 다시 확인해볼 것
def check(time, a, b):
    if 1 not in time[a: b]:
        return True
    return False

count = 0
time = [0] * (max_value + 1) #가능한 회의시간은 0, 사용중이면 1
for i in range(n):
    cost, a, b = data[i]
    if check(time, a, b):
        count += 1
        #회의 시간 배정
        for j in range(a, b):
            time[j] = 1

print(count)