# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 1, 2 를 동시에 수행
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
# 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

N = int(input())
data = [list(map(int, input().split())) for _ in range(N ** 2)]
graph = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# students: 좋아하는 학생 리스트
def simulation(students):
    lst = [] # 비어있는 칸의 수, 좌표
    max_count = 0 #좋아하는 학생의 최대 수
    for x in range(N):
        for y in range(N):
            temp = 0 #x, y 를 기준으로 인접한 좋아하는 학생의 수
            blank = 0 #x, y 를 기준으로 인접한 비어있는 칸의 수
            #비어있는 칸이 아니므로 패스
            if graph[x][y] != 0:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    #비어 있는 칸이라면
                    if graph[nx][ny] == 0:
                        blank += 1
                    #좋아하는 학생인 경우
                    elif graph[nx][ny] in students:
                        temp += 1
            #좋아하는 학생수가 더 많은 좌표인 경우 갱신
            if temp > max_count:
                max_count = temp
                lst = []
                lst.append((blank, x, y))
            elif temp == max_count:
                lst.append((blank, x, y))

    return lst

def get_pos(student):
    for x in range(N):
        for y in range(N):
            if graph[x][y] == student:
                return x, y

for i in range(N ** 2):
    student, like_students = data[i][0], data[i][1:]
    lst = simulation(like_students)
    lst.sort(key=lambda x: (-x[0], x[1], x[2])) #빈칸 많은 순, x, y 작은 순
    # print(lst)
    x, y = lst[0][1], lst[0][2],
    graph[x][y] = student

# print(graph)
#0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
result = 0
score = [0, 1, 10, 100, 1000]
for i in range(N ** 2):
    student, like_students = data[i][0], data[i][1:]
    count = 0 #인접한 좋아하는 학생 수
    x, y = get_pos(student)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] in like_students:
            count += 1

    result += score[count]

print(result)

