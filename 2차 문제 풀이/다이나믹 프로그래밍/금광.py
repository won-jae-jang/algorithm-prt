t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            #첫번째 행일 때
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            #마지막 행일 때
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            
            left = dp[i][j - 1]
            dp[i][j] += max(left_down, left, left_up)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)