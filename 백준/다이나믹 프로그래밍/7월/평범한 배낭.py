n, k = map(int, input().split())

weight = [0] * (n + 1)
value = [0] * (n + 1)

for i in range(1, n + 1):
    weight[i], value[i] = map(int, input().split())

# https://beyond-common-sense.tistory.com/4
