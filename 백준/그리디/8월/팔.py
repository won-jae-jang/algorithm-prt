L, R = map(int, input().split())
result = 1e10
for number in range(L, R + 1):
    if result == 0:
        break

    result = min(result, str(number).count('8'))

print(result)