#연산을 조합하여 문자열로 반환
def concat(n, operator):
    result = '1'
    idx = 0
    for number in range(2, n + 1):
        result += operator[idx]
        result += str(number)
        idx += 1
    return result

def get_info(str):
    numbers = []
    operator = []
    idx = 0
    for i in range(len(str)):
        if str[i].isdigit():
            continue
        else:
            numbers.append(int(str[idx:i]))
            operator.append(str[i])
            idx = i + 1 #i는 연산자이므로 다음번 인덱스는 무조건 숫자

    numbers.append(int(str[idx:])) #마지막 부분 처리
    return numbers, operator

print(get_info('1-2 3+4+5+6+7'.replace(' ', '')))
print('1-2 3+4+5+6+7'.replace(' ', ''))