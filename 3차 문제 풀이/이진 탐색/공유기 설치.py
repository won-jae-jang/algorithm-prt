import sys

input = sys.stdin.readline
n, c = map(int ,input().split())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()
result = 0
start = 1 #최소거리
gap = array[-1] - array[0] #최대 거리
while start <= gap:
    mid = (start + gap) // 2 #공유기와 공유기 사이의 거리
    dist = array[0] + mid
    count = 1 #설치한 공유기 개수
    for i in range(1, n):
        if array[i] >= dist:
            dist = array[i] + mid #다음 공유기 설치 가능 위치
            count += 1
    #설치 제한 개수보다 더 많은 공유기를 설치한 경우
    if count >= c:
        start = mid + 1
        result = mid
    else:
        gap = mid - 1

print(result)