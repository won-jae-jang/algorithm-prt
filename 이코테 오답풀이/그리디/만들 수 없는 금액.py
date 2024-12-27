n = int(input())
data = list(map(int, input().split()))

data.sort()
result = 1
for i in range(n):
    if result >= data[i]:
        result += data[i]
    else:
        break
print(result)
    
