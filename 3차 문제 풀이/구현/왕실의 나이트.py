input_data = input()
y = ord(input_data[0]) - ord('a') + 1
x = int(input_data[1])

movement = [(-1, 2), (1, 2), (-1, -2), (1, -2), 
            (-2, -1), (-2, 1), (2, -1), (2, 1)]

count = 0
for i in range(8):
    nx = x + movement[i][0]
    ny = y + movement[i][1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)