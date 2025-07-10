n = int(input())
plus = []
minus = []
zero_cnt = 0 #0의 개수

for i in range(n):
    num = int(input())
    if num > 0:
        plus.append(num)
    elif num == 0:
        zero_cnt += 1
    else:
        minus.append(num)

plus.sort() #오름차순 정렬
minus.sort(reverse=True) #내림차순 정렬
result = 0
#양수 처리
while len(plus) >= 2:
    first = plus.pop()
    second = plus.pop()
    if first == 1 or second == 1:
        result += first + second
    else:
        result += (first * second)
#음수 처리
while len(minus) >= 2:
    first = minus.pop()
    second = minus.pop()
    result += (first * second)
#양수의 값이 1개 남는경우
if len(plus) == 1:
    result += plus[0]
#음수의 값이 1개 남는 경우
if len(minus) == 1:
    #0의 개수가 없는 경우 더해줌 (0이 있다면 음수를 0과 곱해서 0이 되므로 넘어감)
    if zero_cnt == 0:
        result += minus[0]

print(result)