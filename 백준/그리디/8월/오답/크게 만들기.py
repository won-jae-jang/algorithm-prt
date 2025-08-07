N, K = map(int, input().split())
data = list(input())
stack = []

for i in range(N):
    for j in range(K):
        if stack and int(data[i]) > int(stack[-1]):
            stack.pop()
            K -= 1
        else:
            break

    stack.append(data[i])

if K == 0:
    print(''.join(stack))
else:
    result = ''.join(stack)
    print(result[:-K])