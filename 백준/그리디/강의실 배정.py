n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x:(x[0], x[1]))
count = 1
end = 0 #최소 종료 시간에 대한 인덱스
#Todo (1, 100) (2, 3) (3, 4) -> 3개 고려려
for i in range(1, n):
    #최소 종료시간이 현재 강의 시작 시간보다 크다면
    if data[end][1] > data[i][0]:
        count += 1
    else:
        end += 1

print(count)