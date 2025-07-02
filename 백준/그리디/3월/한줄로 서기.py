n = int(input())
data = list(map(int, input().split()))
result = [n + 1] * (n) 

# i + 1은 해당 사람의 키
for i in range(n):
    count = 0 #자신보다 키가 큰 사람의 수
    for j in range(n):
        #자신보다 키가 큰 사람의 수가 일치하는 경우
        if count == data[i]:
            while (i + 1) > result[j]:
                j += 1
            result[j] = i + 1
            break
        #자신의 키보다 더 큰 경우
        if (i + 1) < result[j]:
            count += 1

for x in result:
    print(x, end=' ')