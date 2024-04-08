place = input()

init_alphabet = place[0]
# 수평이 x, 수직이 y
x = int(ord(place[0]) - ord('a')) + 1
y = int(place[1])

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0

for step in steps:

  nx = x + step[0]
  ny = y + step[1]

  if nx < 1 or ny < 1 or nx > 8 or ny > 8:
    continue
  count += 1

print(count)
  