n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

width = 0
if cranes[0] < boxes[0]:
    width = -1
else:
    while boxes:
        width += 1
        for crane in cranes:
            if boxes and boxes[-1] > crane:
                continue
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break

print(width)