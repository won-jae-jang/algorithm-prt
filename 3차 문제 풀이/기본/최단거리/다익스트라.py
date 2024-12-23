import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

#노드, 간선 개수
n, m = 6, 11 
#시작 노드
start = 1
#각 노드에 연결되어 있는 노드에 대한 정볼르 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된적 있는 경우 무시
        if distance[now] < dist:
            continue
        #현재 노드와 인접한 노드들을 확인인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    #도달할 수 없는 경우
    if distance[i] == INF:
        print('inf')
    #도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])