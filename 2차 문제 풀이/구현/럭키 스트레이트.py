n = input()
center = len(n) // 2

left = 0
right = 0
for i in range(0, center):
    left += int(n[i])
for i in range(center, len(n)):
    right += int(n[i])

if left == right:
    print('LUCKY')
else:
    print('READY')