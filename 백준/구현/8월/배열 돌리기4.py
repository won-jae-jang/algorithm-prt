from collections import deque
from itertools import permutations
import copy
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

rcs = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rcs.append((r, c, s))

#동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 1e10
#회전 순서 정하기
for comb in permutations(rcs, K):

    copy_arr = copy.deepcopy(graph)
    # 회전 순서에 따라 시뮬레이션
    for r, c, s in comb:
        for i in range(s):
            top_x, top_y = r - s - 1 + i, c - s - 1 + i
            bottom_x, bottom_y = r + s - 1 - i, c + s - 1 - i

            x, y = top_x, top_y
            prv = copy_arr[x][y]
            direction = 0
            while True:
                if direction == 4:
                    break
                nx = x + dx[direction]
                ny = y + dy[direction]
                #방향 전환 조건
                if nx < top_x or nx > bottom_x or ny < top_y or ny > bottom_y:
                    direction += 1
                    continue

                prv, copy_arr[nx][ny] = copy_arr[nx][ny], prv
                x, y = nx, ny

    #최솟값 행 구하기
    for i in range(N):
        result = min(result, sum(copy_arr[i]))

print(result)