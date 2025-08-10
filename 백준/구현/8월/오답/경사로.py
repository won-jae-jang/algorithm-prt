N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

def simulation():
    global result
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        is_road = True
        for y in range(N - 1):
            #현재와 다음 높이가 다른 경우
            if graph[x][y] != graph[x][y + 1]:
                # 경사로를 놓을 수 없다면
                if abs(graph[x][y] - graph[x][y + 1]) != 1:
                    is_road = False
                    break
                # 경사로를 왼쪽 방향으로 놓아야 하는 경우
                if graph[x][y] < graph[x][y + 1]:
                    for j in range(L):
                        idx = y - j
                        if idx < 0 or graph[x][y] != graph[x][idx] or visited[x][idx]:
                            is_road = False
                            break
                        else:
                            visited[x][idx] = True
                # 경사로를 오른쪽 방향으로 놓아야 하는 경우
                elif graph[x][y] > graph[x][y + 1]:
                    for j in range(L):
                        idx = y + j + 1
                        if idx >= N or graph[x][y + 1] != graph[x][idx] or visited[x][idx]:
                            is_road = False
                            break
                        else:
                            visited[x][idx] = True

        if is_road:
            result += 1

simulation()
graph = list(zip(*graph))
simulation()
print(result)