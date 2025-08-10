N = int(input())
crane = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crane.sort(reverse=True)
boxes.sort(reverse=True)

if crane[0] < boxes[0]:
    print(-1)
else:
    result = 0
    while boxes:
        result += 1
        for i in range(N):
            #현재 크레인이 박스의 가장 작은 무게를 들 수 없는 경우
            if boxes and crane[i] < boxes[-1]:
                continue

            for box in boxes:
                #현재 크래인이 자신이 감당할 수 있는 가장 무거운 박스를 내림
                if crane[i] >= box:
                    boxes.remove(box)
                    break

    print(result)