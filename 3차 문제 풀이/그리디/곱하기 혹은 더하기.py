s = input()

result = int(s[0])
for num in s[1:]:
    num = int(num)
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)