s = input()

result = 0
for num in s:
    # print(int(num))
    num = int(num)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)