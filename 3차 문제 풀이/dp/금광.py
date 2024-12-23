for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    d = []
    idx = 0
    for i in range(n):
        d.append(data[idx: idx + m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            #행이 0이라면
            if i == 0:
                up = 0
            else:
                up = d[i - 1][j - 1]
            #마지막 행이라면
            if i == n - 1:
                down = 0
            else:
                down = d[i + 1][j - 1]
            left = d[i][j - 1]
            d[i][j] += max(up, left, down)
    
    max_value = 0
    for i in range(n):
        max_value = max(max_value, d[i][m - 1])
    print(max_value)