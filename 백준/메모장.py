from collections import deque

q = deque()
q.extend([1, 2, 3])
q.extend([4, 5, 6])
q.rotate(1)
print(q)