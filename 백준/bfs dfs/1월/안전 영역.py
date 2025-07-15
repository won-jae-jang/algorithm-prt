import sys
import copy
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = []
min_height = 100
max_height = 1
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    min_height = min(min_height, min(data))
    max_height = max(max_height, max(data))

# print(min_height, max_height)

#특정 높이보다 낮은 지역은 물에 잠김
def rain(graph, height):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                graph[i][j] = 0 #물에 잠김

def dfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[x][y] = 0 #방문 처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] != 0:
            dfs(graph, nx, ny)
    
result = 1
for height in range(min_height, max_height + 1):

    temp = copy.deepcopy(graph)
    rain(temp, height)
    count = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] != 0:
                count += 1
                dfs(temp, i, j)

    result = max(result, count)

print(result)