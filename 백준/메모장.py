from collections import deque
import sys
input = sys.stdin.readline

q = deque([]) #(중요도, target 인가)
q.append((0, True))
q.append((1, True))

print(q[0])
print(q[1])