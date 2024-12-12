n = int(input())
data = list(map(int, input().split()))

data.sort()
target = 1
for coin in data:
    if coin > target:
        break
    target += coin

print(target)