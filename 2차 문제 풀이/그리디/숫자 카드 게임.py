n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

result = -1
for i in range(n):
    result = max(result, min(data[i]))

print(result)