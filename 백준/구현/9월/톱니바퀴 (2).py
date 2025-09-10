from collections import deque
t = int(input())
arr = [deque(list(map(int, input()))) for _ in range(t)]

#n번째 톱니바퀴를 direction 방향으로 회전
def left(n, direction):
    if n <= 0:
        return
    l, r = arr[n - 1],  arr[n]
    #서로 맞닿은 극이 다른 경우 -> 회전
    if l[2] != r[-2]:
        left(n - 1, -direction)
        l.rotate(direction)

#n번째 톱니바퀴를 direction 방향으로 회전
def right(n, direction):
    if n > t:
        return
    l, r = arr[n - 2], arr[n - 1]
    #서로 맞닿은 극이 다른 경우 -> 회전
    if l[2] != r[-2]:
        right(n + 1, -direction)
        r.rotate(direction)

k = int(input())
for _ in range(k):
    num, dir = map(int, input().split())
    left(num - 1, -dir)
    right(num + 1, -dir)
    arr[num - 1].rotate(dir)

result = 0
for i in range(t):
    if arr[i][0] == 1:
        result += 1

print(result)