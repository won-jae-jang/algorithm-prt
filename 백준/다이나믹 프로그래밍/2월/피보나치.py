for tc in range(int(input())):
    n = int(input())

    if n == 2:
        print(1, 1) 
        continue
    elif n == 1:
        print(0, 1)
        continue
    elif n == 0:
        print(1, 0)
        continue


    dp = [0] * (n + 1)
    dp[0] = 1 #0의 개수 카운트
    for i in range(n - 1):
        dp[i + 2] = dp[i] + dp[i + 1]

    print(dp[n], end=' ')

    dp = [0] * (n + 1)
    dp[1] = 1 #1의 개수 카운트
    for i in range(n - 1):
        dp[i + 2] = dp[i] + dp[i + 1]

    print(dp[n])