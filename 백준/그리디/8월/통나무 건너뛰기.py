def diff():
    max_diff = -1e10
    for i in range(n - 1):
        max_diff = max(max_diff, abs(array[i] - array[i - 1]), abs(array[i] - array[i + 1]))
    return max_diff

for tc in range(int(input())):

    n = int(input())
    data = list(map(int, input().split()))
    array = [0] * n #통나무들을 세운 결과
    data.sort()

    start, end = 0, n - 1
    idx = 0
    for i in range(0, n - 1, 2):
        array[start + idx] = data[i]
        array[end - idx] = data[i + 1]
        idx += 1

    #홀수개의 통나무라면 나머지 1개 처리
    if n % 2 == 1:
        array[idx] = data[-1]

    print(diff())