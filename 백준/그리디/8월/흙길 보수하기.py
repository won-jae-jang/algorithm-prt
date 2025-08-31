N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

count = 0 #장판지의 개수
pos = 0 #가장 오른쪽 장판지의 좌표

for start, end in range(N):
    for j in range(start, end):
        if j <= pos:
            continue
        else:
            count += 1
            pos = j + L - 1

print(count)