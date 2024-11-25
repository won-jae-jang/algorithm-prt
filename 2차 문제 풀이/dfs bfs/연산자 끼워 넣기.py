n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e10
min_value = 1e10

def operator(result, index):
    global add, sub, mul, div, max_value, min_value

    if index == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    else:
        if add != 0:
            add -= 1
            operator(result + data[index], index + 1)
            add += 1
        if sub != 0:
            sub -= 1
            operator(result - data[index], index + 1)
            sub += 1
        if mul != 0:
            mul -= 1
            operator(result * data[index], index + 1)
            mul += 1
        if div != 0:
            div -= 1
            operator(int(result / data[index]), index + 1)
            div += 1
        
operator(data[0], 1)
print(max_value)
print(min_value)