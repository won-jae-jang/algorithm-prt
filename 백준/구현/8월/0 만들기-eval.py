#9:40
# n - 1번 만큼 연산자를 선택해줘야함.
# 모든 경우의 수를 고려해야 되기 때문에 백트래킹이 부합
# 연산자들이 주어졌을 때 연산 결과가 0인지 아닌지 체크하는 함수

#문자 식 계산 후 0인지 체크
def check(str):
    if eval(str.replace(' ', '')) == 0:
        return True
    return False

#문자와 연산자 합쳐주기
def get_string(n, operator):
    result = '1'
    idx = 0
    for number in range(2, n + 1):
        result += operator[idx]
        result += str(number)
        idx += 1

    return result

def dfs(count, operator):
    if count == n - 1:
        str = get_string(n, operator)
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
