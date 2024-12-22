from bisect import bisect_left, bisect_right
import sys

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

input = sys.stdin.readline
n, x = map(int, input().split())
array = list(map(int, input().split()))

result = count_by_range(array, x, x)
if result > 0:
    print(result)
else:
    print(-1)