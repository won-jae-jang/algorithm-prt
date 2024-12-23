a = input() #sunday
b = input() #saturday

d = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(b)+ 1):
    d[0][i] = i

for i in range(1, len(a) + 1):
    d[i][0] = i

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        #두 문자가 같다면
        if a[i - 1] == b[j - 1]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1

print(d[-1][-1])