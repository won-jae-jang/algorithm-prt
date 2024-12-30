n = int(input())

ugly = [1]

i2 = i3 = i5 = 0
next2 = 2
next3 = 3
next5 = 5

for i in range(n):
    min_value = min(next2, next3, next5)
    ugly.append(min_value)
    if min_value == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if min_value == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if min_value == next5:
        i5 += 1
        next5 = ugly[i5] * 5
    
print(ugly[n - 1])