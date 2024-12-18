n = int(input())
data = list(map(int, input().split()))
operation = list(map(int, input().split()))

max_value = -1e10
min_value = 1e10
#index 1 부터 시작
def dfs(result, index):
    global max_value, min_value
    if index == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    #더하기
    if operation[0] != 0:
        operation[0] -= 1
        dfs(result + data[index], index + 1)
        operation[0] += 1
    #빼기
    if operation[1] != 0:
        operation[1] -= 1
        dfs(result - data[index], index + 1)
        operation[1] += 1
    #곱하기
    if operation[2] != 0:
        operation[2] -= 1
        dfs(result * data[index], index + 1)
        operation[2] += 1
    #나누기
    if operation[3] != 0:
        operation[3] -= 1
        if result > 0:
            dfs(result // data[index], index + 1)
        else:
            dfs(((result * -1) // data[index]) * -1, index + 1)
        # dfs(int(result / data[index]), index + 1)
        operation[3] += 1

dfs(data[0], 1)
print(max_value)
print(min_value)