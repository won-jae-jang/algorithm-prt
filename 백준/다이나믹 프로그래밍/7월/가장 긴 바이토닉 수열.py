n = int(input())
s = list(map(int, input().split()))

total = [0] * n

def LIS(sequence):
    array = [0] * n
    for i in range(n):
        array[i] = 1
        #left
        for j in range(i):
            if sequence[i] > sequence[j]:
                array[i] = max(array[i], array[j] + 1)
    return array

left = LIS(s)
s.reverse()
right = LIS(s)

for i in range(n):
    total[i] = left[i] + right[n - 1 -  i] - 1

# print(left, right)
print(max(total))