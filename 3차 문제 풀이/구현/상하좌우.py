n = int(input())

plan = ['L', 'R', 'U', 'D']
move = [(0, -1), (0, 1), (-1 , 0), (1, 0)]

directions = list(input().split())
x, y = 0, 0
for direction in directions:
    for i in range(4):
        if plan[i] == direction:
            dx, dy = move[i]
            nx = x + dx
            ny = y + dy
            break
    if 0 <= nx < n and 0 <= ny < n:
        x = nx
        y = ny

print(nx + 1, ny + 1)