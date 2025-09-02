#1. x의 개수가 0의 개수와 같거나 1만큼 커야된다.
#2. 체스판이 가득찼거나 가로, 세로, 대각선 빙고가 완성되야함

def check(x, arr):
    #가로: [0, 1, 2] [3, 4, 5], [6, 7, 8]
    #세로: [0, 3, 6], [1, 4, 7], [2, 5, 8]
    #대각선: [0, 4, 8], [2, 4, 6]

    #가로
    if arr[:3].count(x) == 3 or arr[3:6].count(x) == 3 or arr[6:].count(x) == 3:
        return True
    #세로
    if ((arr[0] + arr[3] + arr[6]).count(x) == 3 or (arr[1] + arr[4] + arr[7]).count(x) == 3
            or (arr[2] + arr[5] + arr[8]).count(x) == 3):
        return True
    #대각선
    if (arr[0] + arr[4] + arr[8]).count(x) == 3 or (arr[2] + arr[4] + arr[6]).count(x) == 3:
        return True

    return False

#X.OO..X..
while True:
    arr = input()
    if arr == 'end':
        break
    # XXXOO.XXX
    x = arr.count('X')
    o = arr.count('O')
    blank = arr.count('.')

    #1. x의 개수가 0의 개수와 같거나 1만큼 커야된다. <- 위반
    if x - o > 1 or x - o < 0:
        print('invalid')
        continue

    #2. 가로, 세로, 대각선 빙고가 완성된 경우
    x_bingo = check('X', arr)
    o_bingo = check('O', arr)
    if x_bingo and o_bingo:
        print('invalid')
    elif x_bingo and not o_bingo:
        if x - o == 1: print('valid')
        else: print('invalid')
    elif not x_bingo and o_bingo:
        if x - o == 0: print('valid')
        else: print('invalid')
    elif not x_bingo and not o_bingo and blank == 0:
        print('valid')
    else:
        print('invalid')
