for tc in range(int(input())):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    data.sort()
    interview = n + 1
    result = 0
    for p_score, i_score in data:
        if i_score < interview:
            interview = i_score    
            result += 1

    print(result)