N, K = map(int, input().split())
data = list(map(int, input().split()))
diff = []
for i in range(1, N):
    diff.append(data[i] - data[i - 1])

diff.sort(reverse=True)
result = sum(diff)
for i in range(K - 1):
    result -= diff[i]

print(result)