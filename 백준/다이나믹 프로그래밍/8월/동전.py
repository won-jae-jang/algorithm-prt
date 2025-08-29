for tc in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input()) #target
    dp = [0] * (money + 1)
    dp[0] = 1

    for x in coin:
        for i in range(money + 1):
        # i원의 금액을 만들 수 있는 경우
            if 0 <= (i - x) <= money and dp[i - x] != 0:
                dp[i] += dp[i - x]

