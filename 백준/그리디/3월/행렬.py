n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input())))

for i in range(n):
    b.append(list(map(int, input())))

#x, y를 기준으로 3 * 3 범위의 수를 뒤집는 함수수
def reverse(array, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            array[i][j] = 0 if array[i][j] == 1 else 1

count = 0 #뒤집는 횟수
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            reverse(a, i, j)
            count += 1

same = True #두 행렬이 같은지 여부 
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            same = False

if same:
    print(count)
else:
    print(-1)