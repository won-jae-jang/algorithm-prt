n, k = map(int, input().split())
numbers = input()

stack = []
for num in numbers:
    #스택에 값이 존재하고 차감 가능한 상황일 때
    while stack and k > 0 and int(stack[-1]) < int(num):
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))