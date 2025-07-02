for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data.append(0) #마지막 주식값 처리를 위해

    max_value = 0
    result = 0
    for i in range(n - 1, -1, -1):
        if data[i] > max_value:
            max_value = data[i]
        else:
            result += max_value - data[i]
            
    print(result)