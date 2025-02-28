from collections import deque

s = []
for _ in range(4):
    s.append(deque(list(input())))
k = int(input())

def left(num, direction):
    if num < 0:
        return
    if s[num][2] != s[num + 1][6]:
        left(num - 1, -direction)
        s[num].rotate(direction)

def right(num, direction):
    if num > 3:
        return
    if s[num][6] != s[num - 1][2]:
        right(num + 1, -direction)
        s[num].rotate(direction)

for _ in range(k):
    num, direction = map(int, input().split())
    num -= 1
    left(num - 1, -direction)
    right(num + 1, -direction)
    s[num].rotate(direction)

result = 0
if s[0][0] == '1':
    result += 1
if s[1][0] == '1':
    result += 2
if s[2][0] == '1':
    result += 4
if s[3][0] == '1':
    result += 8

print(result)