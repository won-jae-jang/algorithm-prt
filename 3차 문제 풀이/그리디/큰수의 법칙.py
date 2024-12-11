n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
first = array[-1]
second = array[-2]

result = 0
seq = first * k + second
result = seq * int(m // (k + 1)) + first * (m % (k + 1))
print(result)