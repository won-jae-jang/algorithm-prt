n = int(input())
data = []
max_value = 0
for i in range(n):
    a, b = map(int, input().split())
    max_value = max(max_value, b)
    data.append((a, b)) #회의 소요시간, 시작 시간, 끝나는 시간

data.sort(key=lambda x: (x[1], x[0]))

answer = 0
end_point = 0
for start, end in data:
    if start >= end_point:
        end_point = end
        answer += 1

print(answer)