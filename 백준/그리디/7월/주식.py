for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    result = 0
    max_price = -1
    for i in range(n - 1, -1, -1):
        if data[i] > max_price:
            max_price = data[i]
        else:
            result += (max_price - data[i])

    print(result)