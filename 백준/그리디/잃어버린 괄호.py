n = input()
op = ['+', '-']

# 0009 -> 9
def refine(number):
    if number[0] == '0':
        index = 0
        while number[index] == '0':
            index += 1
        return number[index:]
    return number 

result = 0
number = ''
process = False #초기 음수가 나왔는가 (나왔으면 뒤에 있는 모든 수는 음수 처리)
for alpha in n:
    if alpha not in op:
        number += alpha
    else:
        number = refine(number)
        #앞에 음수 연산이 나온 적이 없고 연산자가 양수인 경우
        if not process:
            result += int(number)        
        elif process:
            result -= int(number)
        #음수 연산이 나온 경우, 그 뒤에 있는 모든 수는 음수 처리
        if alpha == '-':
            process = True
            
        number = ''

#마지막 수
if process:
    result -= int(number)
else:
    result += int(number)

print(result)