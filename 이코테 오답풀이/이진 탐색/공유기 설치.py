n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()
result = 0 #두 공유기 사이의 최대 거리
def binary_search(array, start, end):
    if start > end:
        return None
    global result
    mid = (start + end) // 2 #가장 인접한 두 공유기 사이의 거리
    count = 1 #설치한 공유기 개수
    index = 0
    #설치 가능한 공유기 개수 카운트
    for i in range(1, n):
        if mid <= array[i] - array[index]:
            count += 1
            index = i

    if count < c:
        return binary_search(array, start, mid - 1)
    else:
        result = max(mid, result)
        return binary_search(array, mid + 1, end)
    
binary_search(array, 0, array[-1] - array[0])
print(result)