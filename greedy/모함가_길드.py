n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0 # 총 그룹수
count = 0

# i는 공포도
for i in arr:

  count += 1

  if(count == i):
    result += 1
    count = 0
  
print(result)