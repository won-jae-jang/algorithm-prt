from collections import deque
N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
op = list(map(int, input().split()))

def op1(graph):
    return graph[::-1]

def op2(graph):
    return [row[::-1] for row in graph]

def op3(graph):
    result = list(zip(*graph))
    return op2(result)

def op4(graph):
    result = list(zip(*graph))
    return op1(result)

def split_arr(graph):
    arr1 = [row[:M // 2] for row in graph[:N // 2]]         # 1사분면
    arr2 = [row[M // 2:] for row in graph[:N // 2]]         # 2사분면
    arr3 = [row[M // 2:] for row in graph[N // 2:]]         # 3사분면
    arr4 = [row[:M // 2] for row in graph[N // 2:]]         # 4사분면
    return arr1, arr2, arr3, arr4

def op5(graph):
    result = [[0] * M for _ in range(N)]
    arr1, arr2, arr3, arr4 = split_arr(graph)
    for i in range(N // 2):
        for j in range(M // 2):
            result[i][j] = arr4[i][j]
            result[i][j + M // 2] = arr1[i][j]
            result[i + N // 2][j] = arr3[i][j]
            result[i + N // 2][j + M // 2] = arr2[i][j]
    return result

def op6(graph):
    result = [[0] * M for _ in range(N)]
    arr1, arr2, arr3, arr4 = split_arr(graph)
    for i in range(N // 2):
        for j in range(M // 2):
            result[i][j] = arr2[i][j]
            result[i][j + M // 2] = arr3[i][j]
            result[i + N // 2][j] = arr1[i][j]
            result[i + N // 2][j + M // 2] = arr4[i][j]
    return result

for x in op:
    if x == 1:
        graph = op1(graph)
    elif x == 2:
        graph = op2(graph)
    elif x == 3:
        graph = op3(graph)
        N, M = M, N
    elif x == 4:
        graph = op4(graph)
        N, M = M, N
    elif x == 5:
        graph = op5(graph)
    elif x == 6:
        graph = op6(graph)

for i in range(N):
    print(*graph[i])