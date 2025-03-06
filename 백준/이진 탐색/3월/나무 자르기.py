import sys

input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = int(1e9)
result = 0
#binary search
while start <= end:
    #높이
    height = (start + end) // 2
    total = 0 #얻은 나무
    for tree in trees:
        if tree - height > 0:
            total += (tree - height)

    if total >= m:
        result = height
        start = height + 1
    else:
        end = height - 1

print(result)