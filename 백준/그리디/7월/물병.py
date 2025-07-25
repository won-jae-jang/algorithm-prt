n, k = map(int, input().split())
count = 0

while bin(n).count('1') > k:
    n += 1 #물병 1개 더 구매
    count += 1

print(count)