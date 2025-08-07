#1. combination
# from itertools import combinations
# N, M = map(int, input().split())
# numbers = [i for i in range(1, N + 1)]
# for lst in combinations(numbers, M):
#     for x in lst:
#         print(x, end=' ')
#     print()

#2. back tracking
N, M = map(int, input().split())
numbers = [i for i in range(1, N + 1)]
result = []
visited = [False] * (N + 1)
comb_lst = []
def dfs(n, comb_lst):
    #m개의 수열을 찾은 경우
    if n == M:
        result.append(comb_lst[:])
        return

    for number in range(1, N + 1):
        if not visited[number]:
            #조합 리스트가 비어 있거나 조합의 마지막수보다 더 큰 경우 (중복을 피하기 위함: 1,2 3 = 3, 2, 1)
            if not comb_lst or comb_lst[-1] < number:
                comb_lst.append(number)
                visited[number] = True
                dfs(n + 1, comb_lst)
                comb_lst.remove(number)
                visited[number] = False

dfs(0, comb_lst)
for lst in result:
    print(*lst)