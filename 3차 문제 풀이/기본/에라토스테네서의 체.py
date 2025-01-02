import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for _ in range(n + 1)]

#에라토스테네서의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    #i가 소수인 경우
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

#모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')