n = int(input())
data = []
for i in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for x in data:
    print(x[0])