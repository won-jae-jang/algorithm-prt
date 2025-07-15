#백트래킹
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result = 1e10
visited = [False] * n
#count는 팀의 수
def dfs(count, idx):
    global result
    #팀이 구성이 된 경우
    if count == n / 2:
        team_start = 0
        team_link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                   team_start += graph[i][j]

                elif not visited[i] and not visited[j]:
                    team_link += graph[i][j]
                    
        result = min(result, abs(team_start - team_link))
        return
    
    #팀 구성
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(count + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(result)        