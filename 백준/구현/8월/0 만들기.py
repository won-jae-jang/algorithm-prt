#9:40
# n - 1번 만큼 연산자를 선택해줘야함.
# 모든 경우의 수를 고려해야 되기 때문에 백트래킹이 부합
# 연산자들이 주어졌을 때 연산 결과가 0인지 아닌지 체크하는 함수

def check(str):
    numbers, operator = get_info(str)
    result = numbers[0]
    idx = 0
    # print(str, numbers, operator)
    for i in range(1, len(numbers)):
        if operator[idx] == '+':
            result += numbers[i]
        else:
            result -= numbers[i]
        idx += 1

    if result == 0:
        return True
    return False

def get_info(str):
    numbers = []
    operator = []
    concat_str = str.replace(' ', '') #숫자 이어붙이기
    idx = 0
    for i in range(len(concat_str)):
        if concat_str[i].isdigit():
            continue
        else:
            numbers.append(int(concat_str[idx:i]))
            operator.append(concat_str[i])
            idx = i + 1 #i는 연산자이므로 다음번 인덱스는 무조건 숫자

    numbers.append(int(concat_str[idx:])) #마지막 부분 처리
    return numbers, operator

def get_string(n, operator):
    result = '1'
    idx = 0
    for number in range(2, n + 1):
        result += operator[idx]
        result += str(number)
        idx += 1

    return result

def dfs(count, operator):
    # print(operator)
    if count == n - 1:
        str = get_string(n, operator)
        # print(operator, str)
        if check(str):
            result.append(str)
        return
    # 연산자의 개수는 n - 1개
    operator.append('+')
    dfs(count + 1, operator)
    operator.pop()
    operator.append('-')
    dfs(count + 1, operator)
    operator.pop()
    operator.append(' ')
    dfs(count + 1, operator)
    operator.pop()

for tc in range(int(input())):
    n = int(input())
    result = []
    dfs(0, [])
    result.sort()
    for express in result:
        print(express)
    print()
