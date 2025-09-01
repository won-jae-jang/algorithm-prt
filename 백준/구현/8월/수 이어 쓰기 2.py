n, k = map(int, input().split())

start = 0
digit = 1 #자리수
nine = 9

while k > nine * digit:
    k -= nine * digit
    start += nine
    nine *= 10
    digit += 1

result = start + 1 + (k - 1) // digit
if result > n: print(-1)
else: print(str(result)[(k - 1) % digit])