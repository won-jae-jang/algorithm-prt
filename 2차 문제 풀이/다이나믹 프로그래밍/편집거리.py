a = input()
b = input() #target

n = len(b) #right 
m = len(a) #down
d = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, n + 1):
    d[0][i] = i
for i in range(1, m + 1):
    d[i][0] = i

for i in range(1, m + 1): #a
    for j in range(1, n + 1): #b
        if a[i - 1] == b[j - 1]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])

print(d[m][n])