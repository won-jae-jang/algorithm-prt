n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

team = []

def get_score(graph, team):
    score = 0
    n = len(team)
    for i in range(n):
        for j in range(i + 1, n):
            score += graph[team[i]][team[j]] + graph[team[j]][team[i]]

    return score

# print(get_score(graph, [0, 2, 5]))
# print(get_score(graph, [1, 3, 4]))

# print(get_score(graph, [0, 1, 3, 4]))
# print(get_score(graph, [2, 5, 6, 7]))
