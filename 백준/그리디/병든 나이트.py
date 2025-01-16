# https://afterdawncoding.tistory.com/202
n, m = map(int, input().split()) #세로, 가로
chess = [[0] * (m + 1) for _ in range(n + 1)]

x, y = n , 1 #시작 좌표
count = 1
move = [(-2, 1), (2, 1), (-1, 2), (1, 2)]

def process(idx, x, y):
    global count
    nx = x + move[idx][0]
    ny = y + move[idx][1]
    if 1 <= nx <= n and 1 <= ny <= m:
        x = nx
        y = ny
        count += 1
        return x, y
    return x, y

#이동 방법을 모두 한 번씩 사용 가능한지 체크
for i in range(4):
    x, y = process(i, x, y)

while True:
    moved = False
    for i in range(4):
        nx, ny = process(i, x, y)
        if nx != x and ny != y:
            moved = True
            x, y = nx, ny
            break

    if not moved:
        break

print(count)