n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0
for fear in data:
    count += 1 #모험가 인원 추가
    if count >= fear:
        result += 1
        count = 0

print(result)