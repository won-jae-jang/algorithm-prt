array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 #각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        #실행결과: 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
        print(i, end=' ')