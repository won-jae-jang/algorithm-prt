n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

count = 0
if cranes[0] < boxes[0]:
    count = -1
else:
    while boxes:
        count += 1
        for crane in cranes:
            if boxes and boxes[-1] > crane:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break

print(count)