import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
# dp[i][j]는 i 번째에서 j번째의 수열이 폴란드롬인가를 가르킴. 0 = false, 1 = true
dp = [[0] * n for _ in range(n)]

#자기 자신은 무조건 폴란드롬
for i in range(n):
    dp[i][i] = 1

#첫번째수와 두번째수가 같으면 폴란드롬
for i in range(n - 1):
    if seq[i] == seq[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

#3이상 수열인 벌어지는 경우에는 처음과 끝이 같은지 & 가운데가 폴란드롬인가를 체크
for gap in range(n - 2):
    for left in range(n - gap - 2):
        right = left + 2 + gap
        if seq[left] == seq[right] and dp[left + 1][right - 1] == 1:
            dp[left][right] = 1

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])