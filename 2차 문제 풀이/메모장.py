lst = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]

n, m = 3, 4
result = []
for i in range(n):
    result.append(lst[i * m: i * m + m])

print(result)