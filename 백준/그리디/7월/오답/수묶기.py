n = int(input())
minus = []
plus = []
zero = 0

for i in range(n):
    num = int(input())
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zero += 1

plus.sort()
minus.sort(reverse=True)
result = 0

while len(plus) >= 2:
    first = plus.pop()
    second = plus.pop()
    if first == 1 or second == 1:
        result += first + second
    else:
        result += first * second

while len(minus) >= 2:
    first = minus.pop()
    second = minus.pop()
    result += first * second

left_minus = 0
left_plus = 0
if len(minus) == 1:
    left_minus = minus.pop()
if len(plus) == 1:
    left_plus = plus.pop()

if zero >= 1:
    left_minus = 0

result += left_minus + left_plus
print(result)
