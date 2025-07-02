n = int(input())

lst = []
for i in range(n):
    start, end = map(int, input().split())
    lst.append((end, start))

lst.sort()
result = 0 #회의실의 수
prv_end = 0
# print(lst)
for end, start, in lst:
    #이전 회의가 마무리 된 시간보다 크거나 같아야지 회의 진행 가능
    if prv_end <= start:
        prv_end = end
        result += 1
    else:
        continue

print(result)