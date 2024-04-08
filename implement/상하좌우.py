n = int(input()) # 지도 크기 (n x n)
plans = input().split() # 계획 ['R', 'R', 'L' ...]

# left, right -> y | up, down -> x
dx = [0 , 0, -1, 1] 
dy = [-1 , 1, 0, 0] 
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1

for plan in plans:

  for i in range(len(move_types)):

    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
      continue

  x = nx
  y = ny

print(x, y)