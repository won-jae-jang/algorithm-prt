s = input()

# 0,1일 때 더하고 나머지는 다 곱
# 만약에 이전 연산 결과가 0이라면 무조건 더하기
result = 0

for number in s:

    if result == 0 or int(number) <= 1:
        result += int(number)

    else:
        result *= int(number)
      
print(result)