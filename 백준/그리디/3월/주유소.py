n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 10001
result = price[0]
for i in range(n - 1):
    if price[i] < min_price:
        min_price = price[i]
    result += min_price * road[i]

print(result)