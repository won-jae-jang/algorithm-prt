import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = sum(data)

if n <= m:
     print(max(data))

else:
     #bluelay를 타깃으로 이진탐색 진행
     while start <= end:
          mid = (start + end) // 2

          partial_sum = 0 #한개의 블루레이에 담겨있는 녹화 길이
          count = 1 #사용한 블루레이 개수
          for x in data:
               #해당 블루레이에 녹화 강의를 더 넣을 수 있는 경우
               if partial_sum + x <= mid:
                    partial_sum += x          
               #해당 블루레이가 꽉찬 경우 새로운 블루레이 할당
               else:
                    count += 1
                    partial_sum = x 

          #한개당 블루레이의 크기가 커서 여유가 있는 경우
          if count <= m:
               result = mid
               end = mid - 1
          else:
               start = mid + 1

     print(result)