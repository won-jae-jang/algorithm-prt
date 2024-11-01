n, k = map(int, input().split())

count = 0
while True:
    #(n == k로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # n이 k보다 작을때 (더이상 나눌수 없을 때) 탈출
    if n < k:
        break
    #k로 나누기
    count += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기 (나누어 떨어질 때 1을 더했기 때문)
# count += (n - 1)
count -= 1
print(count)