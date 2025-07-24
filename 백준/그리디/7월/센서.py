n = int(input())
k = int(input())
data = list(map(int, input().split()))
data.sort()
if k >= n:
    print(0)
else:
    dist = []
    for i in range(1, len(data)):
        dist.append(data[i] - data[i - 1])

    dist.sort()
    # print(dist)
    for i in range(k - 1):
        dist.pop()

    print(sum(dist))
