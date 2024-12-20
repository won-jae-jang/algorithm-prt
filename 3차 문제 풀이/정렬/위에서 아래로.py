n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
data.reverse()
for x in data:
    print(x, end=' ')