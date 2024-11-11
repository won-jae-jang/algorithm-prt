from itertools import combinations

n, m = map(int, input().split())
data = []
house = []
chicken = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for x in range(n):
    for y in range(n):
        if data[x][y] == 1:
            house.append((x, y))
        elif data[x][y] == 2:
            chicken.append((x, y))

cases = list(combinations(chicken, m))
result = int(1e9)
for case in cases:
    temp_result = 0
    for hx, hy in house:
        dist = int(1e9)
        for cx, cy in case:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        temp_result += dist
    result = min(result, temp_result)

print(result)