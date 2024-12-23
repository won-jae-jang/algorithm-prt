n, m = map(int, input().split())
INF = int(1e9)
coin = []
d = [INF] * (10001)
d[0] = 0
for i in range(n):
    x = int(input())
    coin.append(x)
    d[x] = 1

for x in coin:
    for i in range(x, m + 1):
        if d[i - x] != INF:
            d[i] = min(d[i], d[i - x] + 1)

if d[m] == INF:
    print(-1)
else:
    print(d[m])