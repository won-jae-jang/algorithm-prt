n, m = map(int, input().split())
result = []
for i in range(n):
    data = list(map(int, input().split()))    
    result.append(min(data))

print(max(result))