n = int(input())
arr = list(map(int, input().split()))
k = int(input())

def dfs(num, arr):
    arr[num] = -2 #방문할 수 없음을 표시
    for i in range(n):
        #현재 노드를 부모로 가지고 있는 자식 노드 i
        if arr[i] == num:
            dfs(i, arr)

dfs(k, arr)
result = 0
for i in range(n):
    if arr[i] != -2 and i not in arr:
        result += 1

print(result)