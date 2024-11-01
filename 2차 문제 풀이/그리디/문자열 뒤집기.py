s = input()

zero = 0
one = 0
prv = int(s[0])
if prv == 0:
    zero += 1
else:
    one += 1

for num in s:
    num = int(num)
    if num == 0 and num != prv:
        zero += 1
        prv = 0
    elif num == 1 and num != prv:
        one += 1
        prv = 1

print(min(zero, one))
