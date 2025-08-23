# 0, 1, 2, 3, 4, 5
# A, B, C, D, E, F
# (0, 5) (1, 3) (2, 4)
# (A, F) (B, D) (C, E)
# EX) (A, F) 가 윗면 아랫면에 위치해 있을 경우 나머지 B, C, D, E 중에서 가장 큰 수를 고른다.
# 첫번째 주사위의 6가지 배치로 모든 경우의 수가 결정된다.

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
pair = {0:5, 5:0, 1:3, 3:1, 2:4, 4:2}

#현재 주사위에서 윗면, 아랫면이 결정됐을 때 가장큰 옆면의 수를 반환
def get_max_num(dice, up, down):
    result = 0
    for i in range(6):
        if dice[i] != up and dice[i] != down:
            result = max(result, dice[i])
    return result

#특정 값이 속하는 주사위 인덱스를 가져옴
def get_idx(dice, value):
    for i in range(6):
        if dice[i] == value:
            return i

def get_up_value(dice, down_value):
    down_idx = get_idx(dice, down_value)
    up_idx = pair[down_idx]
    return dice[up_idx]

result = 0
for i in range(6):
    prv_down = dice[0][i]
    prv_up = get_up_value(dice[0], prv_down)
    temp = get_max_num(dice[0], prv_up, prv_down)
    for j in range(1, N):
        down = prv_up
        up = get_up_value(dice[j], down)
        temp += get_max_num(dice[j], up, down)
        prv_down, prv_up = down, up

    result = max(result, temp)

print(result)