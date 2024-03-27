# n은 볼링공 개수, m은 볼링공의 종류
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 514, 317

'''
주어진 볼링: 1 3 2 3 2 (n=5, m=3)
array = [0, 1, 2, 2]

1차: n = 5 - 1 = 4, result = 0 + 1 * 4 = 4
2차: n = 4 - 2 = 2, result = 4 + 2 * 2 = 8
3차: n = 2 - 2 = 0, result = 8 + 0 * 0 = 8
'''

array = [0] * 11

for x in data:
  # 각 무게에 해당하는 볼링공 개수 카운트
  array[x] += 1 

result = 0

for i in range(1, m + 1):

  n -= array[i] # b가 뽑을 수 있는 공
  result += array[i] * n

print(result)