'''
0. 행, 열마다 지나갈 수 있는지 체크
1. 해당 행 혹은 열의 좌표를 기준으로 상하 / 좌우에 경사로를 놓을 수 있는 지 확인.
2. 길이가 맞지 않은데 경사로를 설치할 수 없다면 해당 행 혹은 열은 건널 수 없는 길이다.
'''

def find(ways):
    visited = [False] * N

    for i in range(1, N):
        if abs(ways[i - 1] - ways[i]) > 1:
            return False

        #왼쪽이 더 큰 경우
        if ways[i - 1] > ways[i]:
            for j in range(L):
                if i + j >= N or ways[i] != ways[i + j] or visited[i + j]:
                    return False
                visited[i + j] = True

        #오른쪽이 더 큰 경우
        elif ways[i - 1] < ways[i]:
            for j in range(L):
                if i - 1 - j < 0 or ways[i - 1] != ways[i - 1 - j] or visited[i - 1 - j]:
                    return False
                visited[i - 1 - j] = True

    return True

N, L = map(int, input().split())
ways = list(list(map(int, input().split())) for _ in range(N))
cross = list(zip(*ways))

result = 0
for i in range(N):
    if find(ways[i]):
        result += 1
    if find(cross[i]):
        result += 1

print(result)




