n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = 0
while True:
    for i in range(k):
        result += data[-1]
        m -= 1
        if m == 0:
            break
    result += data[-2]
    m -= 1
    if m == 0:
        break
    
print(result)