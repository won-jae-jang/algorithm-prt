import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0 #answer

for idx in range(n):
     target = data[idx]
     start = 0
     end = n - 1

     #binary search
     while start < end:

          if start == idx:
               start += 1
               
          if end == idx:
               end -= 1

          if start == end:
               break

          sum_value = data[start] + data[end]

          if sum_value == target:
               count += 1
               break

          if sum_value > target:
               end -= 1
          else:
               start += 1

print(count)