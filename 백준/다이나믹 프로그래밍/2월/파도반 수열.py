for tc in range(int(input())):

    n = int(input())
    dp = [0] * (n + 1)
    dp[1: 4] = [1, 1, 1]
    dp[4: 6] = [2, 2]
    
    # print(dp)
    if n <= 5:
        print(dp[n])

    else:
        idx = 1
        for i in range(6, n + 1):
            dp[i] = dp[i - 1] + dp[idx]
            idx += 1

        print(dp[n])