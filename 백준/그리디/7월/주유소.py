n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
result = min_price * road[0]

for i in range(1, n - 1):
    #이전 도시의 주유 가격이 방문한 도시 주유 가격보다 저렴한 경우
    if min_price < price[i]:
        result += min_price * road[i]
    #현재 방문한 도시의 주유가격이 더 저렴한 경우
    else:
        min_price = price[i]
        result += min_price * road[i]

print(result)