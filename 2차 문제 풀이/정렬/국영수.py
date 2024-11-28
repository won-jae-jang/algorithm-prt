n = int(input())
# 첫번째 값은 오름차순, 두번째 값은 내림 차순
# f = sorted(e, key = lambda x : (x[0], -x[1]))

data = []
for i in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

data = sorted(data, key = lambda x : (-x[1], x[2], -x[3], x[0]))
for name, kor, eng, math in data:
    print(name)