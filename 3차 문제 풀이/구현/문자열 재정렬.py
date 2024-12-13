s = input()

sum_value = 0
alphabet = []
for string in s:
    if string.isalpha():
        alphabet.append(string)
    else:
        sum_value += int(string)

alphabet.sort()
result = ''.join(alphabet) + str(sum_value)
print(result)