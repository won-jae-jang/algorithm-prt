from collections import deque
N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = []

def check():
    count = 0 #내구도가 0인 칸의 개수
    for i in range(N * 2):
        if belt[i] == 0:
            count += 1
    return count >= K

#로봇이 컨테이너와 함께 오른쪽으로 이동
def move_with_container():
    result = []
    for x in robot:
        if x + 1 == N - 1: #내리는 위치인 경우
            continue
        else:
            result.append(x + 1)

    return result

#로봇이 오른쪽으로 이동할 수 있으면 이동
def move_self():
    result = []
    for x in robot[:]:
        #범위 이내에 있고, 벨트 내구도가 1이상이며 다음칸에 로봇이 없을 때
        if x + 1 <= N - 1 and belt[x + 1] >= 1 and x + 1 not in robot:
            #내리는 칸이 아닌 경우
            if x + 1 != N - 1:
                result.append(x + 1) #다음칸으로 이동
            robot.remove(x)
            belt[x + 1] -= 1 #내구도 감소
        #다음칸에 이동을 못하는 경우
        else:
            result.append(x)

    return result

#올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
def raise_robot():
    if belt[0] > 0:
        robot.append(0) #로봇 올리기
        belt[0] -= 1 #내구도 1 감소

process = 0
while True:
    process += 1
    #1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전 한다.
    belt.rotate(1)
    robot = move_with_container()
    #2. 로봇 이동
    robot = move_self()
    #3. 로봇 올리기
    raise_robot()
    #4. 종료 체크
    if check():
        print(process)
        break



