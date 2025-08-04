str = input()
stack = []
tmp = 1
result = 0

for i in range(len(str)):

    if str[i] == '(':
        tmp *= 2
        stack.append(str[i])

    elif str[i] == '[':
        tmp *= 3
        stack.append(str[i])

    elif str[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        stack.pop()
        if str[i - 1] == '(':
            result += tmp
        tmp //= 2

    elif str[i] == ']':
        if not stack or stack[-1] == '(':
            result = 0
            break
        stack.pop()
        if str[i - 1] == '[':
            result += tmp
        tmp //= 3

if stack:
    print(0)
else:
    print(result)