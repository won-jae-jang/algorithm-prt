import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
total_budget = int(input())
data.sort()

start = 0
end = total_budget
result = 0

if sum(data) <= total_budget:
    print(data[-1])

else:
    while start <= end:
        budget = (start + end) // 2
        total = 0

        for x in data:
            #요구 금액이 상한선보다 높다면
            if x > budget:
                #상한선을 할당
                total += budget
            #요구 금액이 상한선보다 작거나 같으면
            else:
                total += x

        if total > total_budget:
            end = budget - 1
        else:
            result = budget
            start = budget + 1

    print(result)