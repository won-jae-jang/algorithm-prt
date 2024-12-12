from itertools import combinations

n, m = map(int ,input().split())
data = list(map(int, input().split()))
weight = [0] * (m + 1)
for w in data:
    weight[w] += 1

count = 0
for i in range(1, m):
    n -= weight[i]
    count += weight[i] * n
    
print(count)