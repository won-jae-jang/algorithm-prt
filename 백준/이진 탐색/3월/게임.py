x, y = map(int, input().split())
z = 100 * y // x #승률

start = 1
end = x
result = x

if z >= 99:
     print(-1)

else:
     while start <= end:
          mid = (start + end) // 2

          tx = x + mid
          ty = y + mid
          tz = 100 * ty // tx

          if tz != z:
               result = mid
               end = mid - 1
          else:
               start = mid + 1

     print(result)