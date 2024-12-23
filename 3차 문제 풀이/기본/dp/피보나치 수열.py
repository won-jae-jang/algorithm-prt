#메모이제이션: 한번 계산된 결과를 리스트에 저장
d = [0] * 100

def fibo(x):
    #종료 조건
    if x == 1 or x == 2:
        return 1
    #연산되지 않은 결과면
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))