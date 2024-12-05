n = int(input())
ugly = [0] * (n + 1)
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    if next2 == ugly[i]:
        i2 += 1
        next2 = ugly[i2] * 2
    if next3 == ugly[i]:
        i3 += 1
        next3 = ugly[i3] * 3
    if next5 == ugly[i]:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])