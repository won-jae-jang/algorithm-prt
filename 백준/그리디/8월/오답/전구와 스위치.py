import copy
N = int(input())
arr = list(map(int, input()))
target = list(map(int, input()))
INF = 1e10

def switch(n, arr):
    count = 0
    for i in range(1, N):
        # i - 1번째 전구가 target 과 다른경우 스위치를 누름
        if arr[i - 1] != target[i - 1]:
            switch(i, arr)
            count += 1

    else:
        for i in [n - 1, n, n + 1]:
            arr[i] ^= 1

# 1. 첫번째 스위치를 누르는 경우
count1 = 1
arr1 = copy.deepcopy(arr)
switch(0, arr1)
for i in range(1, N):
    # i - 1번째 전구가 target 과 다른경우 스위치를 누름
    if arr1[i - 1] != target[i - 1]:
        switch(i, arr1)
        count1 += 1

# 2. 두번째 스위치를 누르지 않는 경우
count2 = 0
arr2 = copy.deepcopy(arr)
for i in range(1, N):
    # i - 1번째 전구가 target 과 다른경우 스위치를 누름
    if arr2[i - 1] != target[i - 1]:
        switch(i, arr2)
        count2 += 1

if arr1 != target:
    count1 = 1e10
if arr2 != target:
    count2 = 1e10
if count1 == 1e10 and count2 == 1e10:
    print(-1)
else:
    print(min(count1, count2))
