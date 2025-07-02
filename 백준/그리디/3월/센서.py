n = int(input())
k = int(input())
data = list(map(int, input().split()))
data.sort()

dist = [] #센서와 센서 사이의 거리
for i in range(n - 1):
    dist.append(data[i + 1] - data[i])

dist.sort()
print(sum(dist[:n - k]))