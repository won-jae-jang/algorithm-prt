from itertools import combinations
n, m = map(int, input().split())
city = []
home = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        #집의 좌표
        if data[j] == 1:
            home.append((i, j))
        #치킨집의 좌표
        elif data[j] == 2:
            chicken.append((i, j))

    city.append(data)

result = 1e10 #도시의 치킨 거리
for comb in combinations(chicken, m):
    city_chicken_dist = 0 #각 조합에 대한 도시의 치킨 거리
    #모든 집에 대해서 치킨 거리 계산
    for hx, hy in home:
        chicken_dist = 1e10 #하나의 집에 대한 치킨 거리
        #하나의 집에 대해서 모든 치킨집에 대한 거리계산 (치킨 거리를 구하기 위해서)
        for cx, cy in comb:
            temp = abs(hx - cx) + abs(hy - cy)
            chicken_dist = min(chicken_dist, temp)

        #1개의 집에 대해서 치킨 거리가 계산이 완료된 상태
        city_chicken_dist += chicken_dist

    #하나의 치킨집 조합에 대해서 도시의 치킨 거리가 계산이 완료된 상태
    result = min(result, city_chicken_dist)

print(result)