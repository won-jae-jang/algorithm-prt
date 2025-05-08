from collections import deque

q = deque([1,2,3,5,8])
lst = list(map(str, list(q)))

print(lst)
answer = '[' + ','.join(lst) + ']'
print(answer)