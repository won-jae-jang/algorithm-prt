r, c = map(int, input().split())
graph = []
visited = [0] * 26 #모든 알파벳 수는 26개임
for i in range(r):
    graph.append(list(input()))

dx = [-1, 1, 0 ,0]
dy = [0 ,0, -1, 1]
result = 0
def dfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < r) and (0 <= ny < c) and visited[ord(graph[nx][ny]) - 65] == 0:
            #백트래킹
            visited[ord(graph[nx][ny]) - 65] = 1 #해당 알파벳 방문처리
            dfs(nx, ny, count + 1)
            visited[ord(graph[nx][ny]) - 65] = 0 #해당 알파벳 방문취소

visited[ord(graph[0][0]) - 65] = 1
dfs(0, 0, 1)
print(result)