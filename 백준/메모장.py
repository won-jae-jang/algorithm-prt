lst = [0]

while lst:
    for i in range(1, 3):
        print(1)
        for j in range(4, 6):
            print('j: ', j)
            if j == 4:
                lst.pop()