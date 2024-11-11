n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] #원래 맵

for i in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1 #사과 위치 표시

info = []
l = int(input())
for i in range(l):
    x, c = input().split()
    info.append((int(x), c))

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
    
#동남서북 *D + 1 / C - 1 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1 #뱀의 머리의 위치
direction = 0 #초기에는 동쪽을 바라보면서 출발함
q = [(x, y)] #뱀이 차지하고 있는 구역
data[x][y] = 2
time = 0
index = 0 #방향 전환 시간 표시
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #벽에 충돌하지 않은 경우
    if nx >= 1 and nx <= n and ny >= 1 and ny <= n and data[nx][ny] != 2:
        #사과를 마주친 경우
        if data[nx][ny] == 1: 
            data[nx][ny] = 2 #뱀의 구역 표시 
            q.append((nx ,ny))
            
        #이동할 수 있는 공간인 경우
        else:
            data[nx][ny] = 2
            q.append((nx ,ny))
            px, py = q.pop(0)
            data[px][py] = 0
        x, y = nx, ny
    #벽에 부딪힌 경우
    else:
        time += 1
        break
    time += 1
    
    if index < l and info[index][0] == time:
        direction = turn(direction, info[index][1])
        index += 1

print(time)