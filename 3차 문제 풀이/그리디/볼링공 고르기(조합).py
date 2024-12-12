from itertools import combinations

n, m = map(int ,input().split())
data = list(map(int, input().split()))

count = 0
for a, b in combinations(data, 2):
    if a != b:
        count += 1

print(count)