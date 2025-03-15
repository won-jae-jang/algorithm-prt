h, w = map(int, input().split())
board = [[0] * w for _ in range(h)]
block = list(map(int, input().split()))

result = 0
for i in range(1, w - 1):
     left_max = max(block[:i])
     right_max = max(block[i + 1:])
     m = min(left_max, right_max)

     if m > block[i]:
          result += (m - block[i])

print(result)