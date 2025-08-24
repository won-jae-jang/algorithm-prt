# 7:40
# 1초마다 r, c 연산이 수행된다.
# 연산 후 크기가 가장큰 열 또는 행을 기준으로 0을 채워준다. (하나씩 뒤부터)
# 이후 연산에서 0은 무시한다.
# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다
# A[r][c] = k 인 순간을 연산 과장마다 체크
# (수, 등장횟수) -> 등장횟수, 수 순서대로 오름차순 정렬
from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def r_operate():
    new_A = []
    max_length = 0
    for row in A:
        temp = [] #임시 계산 결과
        dic = dict(Counter(row))
        for key in dic.keys():
            temp.append((key, dic[key])) # 수, 등장횟수

        temp.sort(key=lambda x: (x[1], x[0])) # 등장횟수, 수 순서대로 오름차순 정렬
        row = []
        for num, count in temp:
            if num == 0:
                continue
            row.extend([num, count])

        max_length = max(max_length, len(row))
        if max_length > 100: max_length = 100
        new_A.append(row)

    for row in new_A:
        if len(row) < max_length:
            row.extend([0] * (max_length - len(row)))
        if len(row) > 100:
            row = row[:100]

    if len(new_A) > 100:
        return new_A[:100]
    return new_A


def check(arr):
    row = len(arr)
    col = len(arr[0])
    if r - 1 < row and c - 1 < col and arr[r - 1][c - 1] == k:
        return True
    return False

time = 0
while True:
    if check(A):
        print(time)
        break

    if time > 100:
        print(-1)
        break

    row = len(A)
    col = len(A[0])

    if row >= col:
        A = r_operate()
        col, row = len(A[0]), len(A)

    elif row < col:
        A = list(zip(*A))
        A = r_operate() #C연산
        A = list(zip(*A))

    time += 1













