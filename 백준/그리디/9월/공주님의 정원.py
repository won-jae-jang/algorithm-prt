n = int(input())
flowers = []
for i in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    flowers.append((m1 * 100 + d1, m2 * 100 + d2))

flowers.sort()
result = 0
end = 301 #꽃은 3월 1일부터 개화되어야 함
while flowers:
    if end >= 1201 or flowers[0][0] > end:
        break

    temp = 0 #조건에 맞는 다음 꽃들 중에서 가장 늦게 지는 꽃
    for i in range(len(flowers)):
        if flowers[0][0] <= end:
            #더 늦게 지는 꽃인 경우
            if temp < flowers[0][1]:
                temp = flowers[0][1]

            flowers.remove(flowers[0])

    if temp > end:
        end = temp
        result += 1

if end < 1201:
    print(0)
else:
    print(result)