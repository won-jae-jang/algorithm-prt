import sys

input = sys.stdin.readline
n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0
while start <= end:
    mid = (start + end) // 2 #gap
    value = array[0] #설치한 공유기 (첫번 째 공유기는 설치 하고 시작함)
    count = 1 #설치된 공유기 개수
    #공유기 설치
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    #공유기를 더 설치할 수 있는 경우
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)