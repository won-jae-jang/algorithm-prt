import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

start = 0
end = n - 1
# result = abs(data[start] + data[end])
result = float('inf')  # 초기값을 무한대로 설정
features = [data[start], data[end]] #가장 0에 가까운 두 용액의 모임

while start < end:

    sum_value = data[start] + data[end]
    #두 합의 결과가 0에 더욱 가까운 경우
    if abs(sum_value) < result:
        result = abs(sum_value)
        features = [data[start], data[end]]
        if result == 0:
            break
    
    #두 합의 결과가 음수인 경우
    if sum_value < 0:
        start += 1
    #두 합의 결과가 양수인 경우
    else:
        end -= 1

print(features[0], features[1])