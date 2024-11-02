import itertools

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
for a,b in itertools.combinations(data, 2):
    if a != b:
        result += 1

print(result)