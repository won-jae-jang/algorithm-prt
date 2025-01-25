n, m = map(int, input().split())

visited = [] 

def dfs(count):
    if count == m:
        for x in visited:
            print(x, end=' ')
        print()
        return
    
    for i in range(1, n + 1):
        if i not in visited:
            visited.append(i)
            dfs(count + 1)
            visited.pop()

dfs(0)