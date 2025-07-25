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

    three_side = 4 #3개의 면이 노출되는 주사위의 개수
    one_side = (n - 2) * (n - 1) * 4 + (n - 2) ** 2 #1개의 면이 노출되는 주사위의 개수
    two_side = (n - 1) * 4 + (n - 2) *4 #2개의 면이 노출되는 주사위의 개수

    result = 0
    result += three_side * sum(min_dice[:3])
    result += two_side * sum(min_dice[:2])
    result += one_side * min_dice[0]

    print(result)
