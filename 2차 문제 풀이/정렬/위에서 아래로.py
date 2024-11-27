n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data = sorted(data, reverse=True)

for x in data:
    print(x, end=' ')