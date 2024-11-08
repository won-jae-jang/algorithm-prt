n = int(input())
plan = list(input().split())

map = [[0] * (n + 1) for _ in range(n + 1)]
dx = [-1, 1, 0, 0] #북남서동
dy = [0, 0, -1, 1]
x, y = 1, 1

for p in plan:
    if p == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    elif p == 'R':
        nx = x + dx[3]
        ny = y + dy[3]
    elif p == 'U':
        nx = x + dx[0]
        ny = y + dy[0]
    elif p == 'D':
        nx = x + dx[1]
        ny = y + dy[1]
    
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n:
        x = nx
        y = ny

print(x, y)
