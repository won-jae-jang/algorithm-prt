# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.

from collections import deque

def cal_D(n):
    return (n * 2) % 10000

def cal_S(n):
    return 9999 if n == 0 else n - 1

def cal_L(n):
    n = str(n)
    while len(n) != 4:
        n = '0' + n
    #왼쪽으로 회전
    return int(n[1:] + n[0])

def cal_R(n):
    n = str(n)
    while len(n) != 4:
        n = '0' + n
    #오른쪽으로 회전
    return int(n[-1] + n[:-1])

def bfs(a):
    q = deque()
    q.append((a, '')) #result, operator
    visited = [0] * 10001
    visited[a] = True
    while q:
        x, operator = q.popleft()
        if x == b:
            print(operator)
            break

        D, S, L, R = cal_D(x), cal_S(x), cal_L(x), cal_R(x)
        if not visited[D]:
            q.append((D, operator + 'D'))
            visited[D] = True

        if not visited[S]:
            q.append((S, operator + 'S'))
            visited[S] = True

        if not visited[L]:
            q.append((L, operator + 'L'))
            visited[L] = True

        if not visited[R]:
            q.append((R, operator + 'R'))
            visited[R] = True


for tc in range(int(input())):
    a, b = map(int, input().split())
    bfs(a)