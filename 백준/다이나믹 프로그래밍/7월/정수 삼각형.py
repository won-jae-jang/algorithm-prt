n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))
data.reverse()

for i in range(1, n):
    for j in range(len(data[i])):
        data[i][j] += max(data[i - 1][j], data[i - 1][j + 1])

print(data[-1][0])