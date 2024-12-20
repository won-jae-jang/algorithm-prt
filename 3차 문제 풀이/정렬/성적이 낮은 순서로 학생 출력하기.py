n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    data.append((name, int(score)))

data = sorted(data, key= lambda x:x[1])
print(data)