from collections import Counter
from bisect import bisect_left, bisect_right

T = int(input()) # 부 배열의 합으로 만족되야 하는 값
n = int(input()) # 배열 A의 원소 개수
A = list(map(int,input().split())) # 배열 A
m = int(input()) # 배열 B의 원소 개수
B = list(map(int,input().split())) # 배열 B

#풀이1
# c = Counter()
# for start in range(n):
#      for end in range(start + 1, n + 1):
#           c[sum(A[start: end])] += 1 #A의 모든 부분합 구하기

# result = 0
# for start in range(m):
#      for end in range(start + 1, m + 1):
#           t = T - sum(B[start: end])
#           result += c[t]

# print(result)

#풀이2
A_sum, B_sum = [], []
for start in range(n):
     for end in range(start + 1, n + 1):
          A_sum.append(sum(A[start:end]))

for start in range(m):
     for end in range(start + 1, m + 1):
          B_sum.append(sum(B[start:end]))

A_sum.sort()
B_sum.sort()

result = 0
for i in range(len(A_sum)):
     left = bisect_left(B_sum, T - A_sum[i])
     right = bisect_right(B_sum, T - A_sum[i])
     result += right - left

print(result)