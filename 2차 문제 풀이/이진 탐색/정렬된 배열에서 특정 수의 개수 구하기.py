import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n, x = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def count_by_range(a, left_value, right_value):
    left_side = bisect_left(a, left_value)
    right_side = bisect_right(a, right_value)
    return right_side - left_side

result = count_by_range(data, x, x)
if result == 0:
    print(-1)
else:
    print(result)