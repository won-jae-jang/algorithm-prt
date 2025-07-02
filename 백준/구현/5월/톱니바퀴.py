# 10101111
# 01111101
# 11001110
# 00000010
# 2 k
# 3 -1: 3번째 톱니바퀴를 반시계 방향으로 회전
# 1 1: 1번째 톱니바퀴를 시계 방향으로 회전

from collections import deque
one = deque(list(map(int, input())))
two = deque(list(map(int, input())))
three = deque(list(map(int, input())))
four = deque(list(map(int, input())))
lst = [one, two, three, four]

k = int(input())
roll = [tuple(map(int, input().split())) for _ in range(k)]

#왼쪽 수레바퀴를 돌리나
def left(number, dir):
    if number < 0:
        return
    if lst[number][2] != lst[number + 1][-2]:
        left(number - 1, -dir)
        lst[number].rotate(dir)

#오른쪽 수레바퀴를 돌리나
def right(number, dir):
    if number > 3:
        return
    if lst[number][-2] != lst[number - 1][2]:
        right(number + 1, -dir)
        lst[number].rotate(dir)

def get_score():
    score = 0
    if one[0] == 1:
        score += 1
    if two[0] == 1:
        score += 2
    if three[0] == 1:
        score += 4
    if four[0] == 1:
        score += 8
    return score

for number, dir in roll:
    number -= 1
    left(number - 1, -dir)
    right(number + 1, -dir)
    lst[number].rotate(dir)

print(get_score())










