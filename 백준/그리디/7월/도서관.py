n, m = map(int, input().split())
data = list(map(int, input().split()))
minus = []
plus = []
for x in data:
    if x < 0:
        minus.append(x)
    else:
        plus.append(x)

minus.sort()
plus.sort(reverse=True)

flag = 0 #어느 방향을 마지막 위치로 할 것인지 확인
if len(plus) == 0:
    flag = -1
elif len(minus) == 0:
    flag = 1
elif plus[0] > abs(minus[0]):
    flag = 1
else:
    flag = -1

#m번만큼 데이터 뺴기
def pop_m(list):
    for i in range(m):
        if list:
            list.pop(0)
        else:
            break

result = 0
#양수 지점에서 마지막 책을 꽂아넣는 경우
if flag == 1:
    #양수 처리: 끝나는 지점 (편도)
    dist = plus[0]
    result += dist
    pop_m(plus)

#음수 지점에서 마지막 책을 꽂아넣는 경우
else:
    #음수 처리: 끝나는 지점 (편도)
    dist = abs(minus[0])
    result += dist
    pop_m(minus)

# 양수 처리 (왕복)
while plus:
    dist = plus[0]
    result += (dist * 2)
    pop_m(plus)

#음수 처리 (왕복)
while minus:
    dist = abs(minus[0])
    result += (dist * 2)
    pop_m(minus)

print(result)
