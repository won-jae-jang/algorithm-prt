import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
stack = []
result = [0] * n

for i in range(n):
    while stack and stack[-1][0] < numbers[i]:
        value, idx = stack.pop()
        result[idx] = numbers[i] 

    stack.append((numbers[i], i)) #value, idx

for i in range(n):
    if result[i] == 0:
        print(-1, end=' ')
    else:
        print(result[i], end=' ')