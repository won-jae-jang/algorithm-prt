n, k = map(int, input().split())

result = 0
rest = 0

while True:

  if n < k:
    break

  rest += n % k
  n //= k
  result += 1

if(rest != 0):
  result += rest 
  
print(result)