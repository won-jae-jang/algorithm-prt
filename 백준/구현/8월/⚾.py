#7:42
from itertools import permutations
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
player = [x for x in range(1, 9)] #2번 ~ 9번 선수
result = 0

#comb[x] = k -> x 번째 순번에 k 번 타자가 배치
for comb in permutations(player, 8):
    comb = list(comb)
    comb = comb[:3] + [0] + comb[3:] #조합 순서
    idx = 0 #선수 시작 위치
    score = 0 #현재 조합에 따른 점수
    for inning in data:
        #이닝 진행
        base = [0, 0, 0]  # 홈, 1루, 2루, 3루
        out = 0
        while out != 3:
            batter = comb[idx]
            play = inning[batter]

            if play == 0:
                out += 1
            elif play == 1:
                score += base[2]
                base = [1] + base[:2]
            elif play == 2:
                score += base[1] + base[2] #2, 3루
                base = [0, 1, base[0]]
            elif play == 3:
                score += sum(base)
                base = [0, 0, 1]
            elif play == 4:
                score += sum(base) + 1
                base = [0, 0, 0]

            idx = (idx + 1) % 9 #다음 타자 순번 지정

    result = max(result, score)

print(result)