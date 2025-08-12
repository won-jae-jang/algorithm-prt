N = int(input())
before1 = list(map(int, input())) #1번 스위치를 누르지 않은 경우
before2 = before1[:] #1번 스위치를 누른 경우
after = list(map(int, input()))
INF = 1e10

def switch(before):
    count = 0
    #2번 스위치부터 검사
    for i in range(1, N):
        #이전 전구의 상태가 같은 경우
        if before[i - 1] == after[i - 1]:
            continue
        #상태가 달라 스위치를 누른 경우
        count += 1
        for j in [i - 1, i, i + 1]:
            if j < N:
                before[j] = not before[j] #상태 반전

    return count if before == after else INF

#1번 스위치를 누르지 않은 경우
result = switch(before1)
#1번 스위치를 누른 경우
before2[0] = not before2[0]
before2[1] = not before2[1]
result = min(result, switch(before2) + 1)
print(result if result != INF else -1)