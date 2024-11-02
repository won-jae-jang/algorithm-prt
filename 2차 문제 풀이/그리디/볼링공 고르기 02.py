n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * (n + 1)

for i in range(n):
    array[data[i]] += 1

result = 0
for i in range(1, m):
    n -= array[i] #전체 볼링공의 경우의 수에서 a 가 선택한 볼링공을 차감함
    result += array[i] * n

print(result)