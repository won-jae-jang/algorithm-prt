n = int(input())
data = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))


data = sorted(data, key=lambda student:student[1])
for name, score in data:
    print(name, end=' ')