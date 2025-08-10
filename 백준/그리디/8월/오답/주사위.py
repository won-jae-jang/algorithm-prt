n = int(input())
dice = list(map(int, input().split()))
min_dice = []

if n == 1:
    dice.sort()
    print(sum(dice) - dice[-1])
else:
    min_dice.append(min(dice[0], dice[5]))
    min_dice.append(min(dice[1], dice[4]))
    min_dice.append(min(dice[2], dice[3]))
    min_dice.sort()

    #1 ~ 3개의 면을 노출하는 주사위의 개수
    three = 4
    two = 4 * (n - 1) + 4 * (n - 2)
    one = 5 * n ** 2 - (three * 3 + two * 2)

    print(three * sum(min_dice) + two * sum(min_dice[:2]) + one * min_dice[0])
