n = int(input())
row = [0] * n

result = 0
def dfs(x):
    global result
    if x == n:
        result += 1
        return
    #x행 y 열에 대해서 탐색
    for y in range(n):
        #해당 행, 열의 위치가 다른 퀸을 공격하지 않는다면
        if not attack(x, y):
            row[x] = y
            dfs(x + 1)

#x, y 위치에 퀸을 설치할 경우 다른 퀸을 공격하는지 여부
def attack(x, y):

    for i in range(x):
        #같은 열 상에 있는지, 혹은 대각선상에 있는지 체크 (행의 길이 = 열의 길이 -> 대각선)
        if y == row[i] or abs(x - i) == abs(y - row[i]):
            return True

    return False

dfs(0)
print(result)