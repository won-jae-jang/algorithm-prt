str = input()

answer = 0
tmp = 1
stack = []
for i in range(len(str)):
    if str[i] == '(':
        stack.append(str[i])
        tmp *= 2

    elif str[i] == '[':
        stack.append(str[i])
        tmp *= 3

    elif str[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if str[i - 1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2

    elif str[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if str[i - 1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
