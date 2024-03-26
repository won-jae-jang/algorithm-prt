n = int(input())
arr = list(map(int, input().split()))

arr.sort()
target = 1

for coin in arr:

  if target == coin:
    target += coin

  elif target > coin:
    target += coin

  else:
    break

print(target)