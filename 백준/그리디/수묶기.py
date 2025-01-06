n = int(input())
minus = []
plus = []
zero = []

for i in range(n):
    num = int(input())
    if num >= 1:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zero.append(num)

plus.sort(reverse=True) #내림 차순 정렬
minus.sort() #오름차순 정렬

result = 0
while len(plus) >= 2:
    first = plus.pop(0)
    second = plus.pop(0)
    #두수중 하나라도 1이 있다면
    if 1 == first or 1 == second:
        plus.append(first)
        plus.append(second)
        break
    result += (first * second)

while len(minus) >= 2:
    first = minus.pop(0)
    second = minus.pop(0)
    result += (first * second)

#나머지 음수가 있는 경우
if len(minus) != 0:
    #0이 없다면 결과에 더해줌
    if len(zero) == 0:
        result += minus.pop(0)
    #0이 있다면 음수에 0을 곱하여 상쇄

result += sum(plus)
print(result)