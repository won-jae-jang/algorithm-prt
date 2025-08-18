import math

def find_one(n, k):

    if len(answer) == N - 1:
        answer.append(numbers[-1])
        return

    case = math.factorial(n) // n
    sequence = math.ceil(k / case)
    answer.append(numbers.pop(sequence))
    find_one(n - 1, k - case * (sequence - 1))


def find_k():
    n = N
    for num in K:
        case = math.factorial(n) // n
        idx = numbers.index(num)

        if len(numbers) == 2:
            idx += 1
            answer.append(idx)
            return

        answer.append(case * idx)
        numbers.pop(idx)
        n -= 1

N = int(input())
data = list(map(int, input().split()))
problem = data.pop(0)
answer = []
if problem == 1:
    K = data[0]
    numbers = [x for x in range(N + 1)]
    find_one(N, K)
    print(' '.join(map(str, answer)))
else:
    K = data
    numbers = [x for x in range(1, N + 1)]
    find_k()
    print(sum(answer))


