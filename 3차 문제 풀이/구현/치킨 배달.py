from itertools import combinations

n, m = map(int, input().split())
house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

result = 1e9
for chickens in combinations(chicken, m):
    city_dist = 0
    for hx, hy in house:
        chicken_dist = 1e9
        for cx, cy in chickens:
            dist = abs(hx - cx) + abs(hy - cy)
            chicken_dist = min(chicken_dist, dist)
        city_dist += chicken_dist
    result = min(result, city_dist)

print(result)