loc = input()

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

x, y = int(loc[1]), int(ord(loc[0])) - int(ord('a')) + 1

result = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        result += 1

print(result)