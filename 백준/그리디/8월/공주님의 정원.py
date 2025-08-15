#3: 35
N = int(input())
flowers = []
for _ in range(N):
    s_month, s_day, e_month, e_day = map(int, input().split())
    flowers.append((s_month * 100 + s_day, e_month * 100 + e_day))

flowers.sort()
end = 301 #가장 늦게 지는 꽃의 일자
result = 0
while flowers:
    #종료 조건
    if end >= 1201 or flowers[0][0] > end:
        break

    temp = 0
    for _ in range(len(flowers)):
        #조건에 충족하는 꽃들을 모두 제거
        if flowers[0][0] <= end:
            if flowers[0][1] > temp:
                temp = flowers[0][1]
            flowers.remove(flowers[0])
    #새로운 꽃 설치
    if temp > end:
        end = temp
        result += 1

if end < 1201:
    print(0)
else:
    print(result)