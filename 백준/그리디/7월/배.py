n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
time = 0

if cranes[0] < boxes[0]:
    print(-1)
else:
    while boxes:
        for crane in cranes:
            #현재 크레인이 가장 무게가 작은 화물을 옮길수 없는 경우 -> pass
            if boxes and crane < boxes[-1]:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1

    print(time)
