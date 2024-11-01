n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

count = int(m / (k + 1)) * k # 큰수가 곱해지는 횟수
count += m % (k + 1)

result = first * count + second * (m - count)
print(result)