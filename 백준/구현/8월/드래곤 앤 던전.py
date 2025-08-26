# 최대 hp: 몬스터 공격력 * ceil(몬스터 공격력 / 용사 공격력)
import math
end = 0 #max_hp
N, H_atk, = map(int, input().split())
data = []
for i in range(N):
    t, a, h = map(int, input().split())
    data.append((t, a, h))
    #몬스터인 경우
    if t == 1:
        end += a * math.ceil(h / H_atk)

def simulation(max_hp, H_atk):
    cur_hp = max_hp
    for t, a, h in data:
        # 몬스터인 경우
        if t == 1:
            count = math.ceil(h / H_atk) #용사가 몬스터를 죽이기 위해서 필요한 공격 횟수
            cur_hp -= a * (count - 1)
            if cur_hp <= 0:
                return False
        #포션인 경우
        else:
            #현재 용사의 생명력 HCurHP가 일정량 회복
            cur_hp = min(max_hp, cur_hp + h)
            #공격력 HATK도 일정량만큼 증가
            H_atk += a

    #용사가 모든 던전을 클리어 한 경우
    return True

start = 1
result = 0 #최대 용사의 hp
while True:
    if start > end:
        break
    mid = (start + end) // 2
    #현재 hp로 던전을 클리어 할 수 있는 경우
    if simulation(mid, H_atk):
        result = mid
        end = mid - 1 #최소 hp를 찾기 위해서 범위 축소
    #현재 hp로 던전 클리어할 수 없는 경우
    else:
        start = mid + 1 #클리어할 수 있는 hp 탐색

print(result)