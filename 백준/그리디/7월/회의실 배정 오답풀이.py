n = int(input())
data = []
for i in range(n):
    start, end = map(int, input().split())
    data.append((end, start))

data.sort()

result = 0
end_time = -1
for end, start in data:
    if end_time <= start:
        result += 1 
        end_time = end

print(result)