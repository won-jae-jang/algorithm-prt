n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
group = []
for fear in data:
    group.append(fear)
    if len(group) >= fear:
        group = []
        result += 1

print(result)