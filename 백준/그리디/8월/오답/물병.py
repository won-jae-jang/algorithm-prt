N, K = map(int, input().split())

result = 0
while True:
    count = bin(N).count('1') #물병의 개수

    if count > K:
        N += 1
        result += 1
    else:
        print(result)
        break