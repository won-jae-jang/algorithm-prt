n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):

  card = min(arr[i])
  if(card > result) :
    result = card

print(result)