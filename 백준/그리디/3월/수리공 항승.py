n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

width = 1
start = data[0]
end = 0
for i in range(n):
    end = data[i]
    dist = (end - start) + 1
    if dist > l:
        width += 1
        start = data[i]

print(width)