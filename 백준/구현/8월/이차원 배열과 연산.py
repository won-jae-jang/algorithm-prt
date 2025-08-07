from collections import Counter
r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]

col = len(array[0]) #열의 길이
row = len(array) #행의 길이

#r,c 연산: c 연산은 행열을 뒤집고 연산된 결과를 다시 뒤집어주면 된다.
def cal():
    max_length = 0
    new_A = []
    for lst in array:
        temp = []
        dic = dict(Counter(lst)) #숫자: 등장횟수
        for key in dic.keys():
            temp.append((key, dic[key]))
        #등장횟수의 오름차순 -> 수의 오름차순
        temp.sort(key = lambda x: (x[1], x[0]))
        row = []
        for num, count in temp:
            if num != 0:
                row.extend([num, count])
        max_length = max(max_length, len(row))
        #열이 100이 넘어가는 경우
        if max_length > 100: max_length = 100
        new_A.append(row)

    for row in new_A:
        if len(row) < max_length:
            row.extend([0] * (max_length - len(row)))
        if len(row) > 100:
            row = row[:101]
    # 행이 100이 넘어가는 경우
    if len(new_A) > 100:
        return new_A[:101]

    return new_A

time = 0
while True:
    col = len(array[0])  # 열의 길이
    row = len(array)  # 행의 길이

    if r - 1 < row and c - 1 < col and array[r - 1][c - 1] == k:
        print(time)
        break

    if time > 100:
        print(-1)
        break

    #r 연산 수행 조건
    if row >= col:
        array = cal() #r행 연산
        col, row = len(array[0]), len(array)
    #c 연산 수행 조건
    elif row < col:
        array = list(zip(*array)) #행열 뒤집기
        array = cal() #연산후
        array = list(zip(*array)) #다시 뒤집어서 원래 모양 복원

    time += 1