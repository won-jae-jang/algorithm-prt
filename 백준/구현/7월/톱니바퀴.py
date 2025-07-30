#56분
from collections import deque

# w1 = deque(list(input()))
# w2 = deque(list(input()))
# w3 = deque(list(input()))
# w4 = deque(list(input()))
lst = [deque(list(input())) for _ in range(4)]
lst.insert(0, []) #n번째 숫자를 맞추기 위한 삽입

n = int(input())
data = list(map(int, input().split()) for _ in range(n)) #number, direction
# print(lst)
# -> : 2, -2 / <- : -2, 2
#시계 방향: rotate(1) , 반시계: rotate(-1)
# n번째 톱니바퀴를 기준으로 오른쪽에 있는 톱니바퀴를 검사 / n번째 톱니바퀴는 direction으로 회전한다는 뜻
def right(n, direction):
    if n == 4:
        return
    #오른쪽 톱니바퀴가 맞물려 돌아가는 조건
    if lst[n][2] != lst[n + 1][-2]:
        right(n + 1, -direction)
        lst[n + 1].rotate(-direction)

def left(n, direction):
    if n == 1:
        return
    #왼쪽 톱니바퀴가 맞물려 돌아가는 조건
    if lst[n][-2] != lst[n - 1][2]:
        left(n - 1, -direction)
        lst[n - 1].rotate(-direction)

def get_score(lst):
    scores = [0, 1, 2, 4, 8]
    result = 0
    for i in range(1, 5):
        score = scores[i]
        #i번째 톱니바퀴의 12시 방향이 S극인 경우
        if lst[i][0] == '1':
            result += score

    return result

for number, direction in data:
    right(number, direction)
    left(number, direction)
    lst[number].rotate(direction)

# print(lst)
print(get_score(lst))









