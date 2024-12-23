n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            left = 0
        else:
            left = d[i - 1][j - 1]
        if j == len(d[i]) - 1:
            right = 0
        else:
            right = d[i - 1][j]
        d[i][j] += max(left, right)

print(max(d[n - 1]))