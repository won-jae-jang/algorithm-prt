from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, target = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque([]) #(중요도, target 인가)
    for i in range(n):
        if i == target:
            q.append((data[i], True))            
        else:
            q.append((data[i], False))            

    count = 0 #몇번째로 인쇄되는가
    while True:
        
        important, is_target = q[0][0], q[0][1]

        printable = True
        #해당 문서보다 중요도가 높은 문서가 있는지 확인
        for i in range(1, n):
            if important < q[i][0]:
                printable = False
                break
        #프린트 가능한 경우
        if printable:
            q.popleft()
            count += 1
            n -= 1 #문서의 개수 감소
            if is_target:
                break
        #프린트 가능한 X 경우
        else:
            q.popleft()
            q.append((important, is_target))

    print(count)