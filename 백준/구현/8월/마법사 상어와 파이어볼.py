# 질량, 속도, 파이어볼 개수에 대한 배열은 합산으로 표기
# 방향에 대한 배열은 r, c 좌표에 대해서 배열로 저장
import copy

N, M, K = map(int, input().split())
fireball = [[[] for _ in range(N)] for _ in range(N)] #파이어볼

for _ in range(M):
    i, j, m, s, d = map(int, input().split()) # 행 열 질량 방향 속도
    i -= 1
    j -= 1
    fireball[i][j].append((m, s, d))

#합쳐지는 파이어볼의 방향이 모두 홀수인가
def odd(directions):
    for d in directions:
        if d % 2 == 0:
            return False
    return True

#합쳐지는 파이어볼의 방향이 모두 짝수인가
def even(directions):
    for d in directions:
        if d % 2 == 1:
            return False
    return True

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    next_fireball = [[[] for _ in range(N)] for _ in range(N)]
    #1. 모든 파이어볼이
    for x in range(N):
        for y in range(N):
            if len(fireball[x][y]) >= 1:
                # 방향 di로 속력 si칸 만큼 이동
                for m, s, d in fireball[x][y]:
                    nx = (x + dx[d] * s) % N
                    ny = (y + dy[d] * s) % N
                    next_fireball[nx][ny].append((m, s, d))

    fireball = [[[] for _ in range(N)] for _ in range(N)] #이동이 끝난후 파이어볼 리스트 초기화
    for i in range(N):
        for j in range(N):
            #파이어볼이 2개 이상인 칸
            if len(next_fireball[i][j]) >= 2:
                concat_m = 0 #합쳐진 질량
                concat_s = 0 #합쳐진 속력
                temp = [] #방향을 담을 임시 저장소
                for m, s, d in next_fireball[i][j]:
                    concat_m += m
                    concat_s += s
                    temp.append(d) #방향 정보

                split_m = concat_m // 5 #질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
                #4.질량이 0인 파이어볼은 소멸
                if split_m == 0:
                    continue
                split_s = concat_s // len(next_fireball[i][j]) # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋
                #합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수
                if even(temp) or odd(temp):
                    for d in [0, 2, 4, 6]:
                        fireball[i][j].append((split_m, split_s, d))
                else:
                    for d in [1, 3, 5, 7]:
                        fireball[i][j].append((split_m, split_s, d))
            #파이어볼이 1개인 칸
            elif len(next_fireball[i][j]) == 1:
                fireball[i][j].append(next_fireball[i][j].pop())

result = 0
for i in range(N):
    for j in range(N):
        if len(fireball[i][j]) >= 1:
            for m, s, d in fireball[i][j]:
                result += m

print(result)