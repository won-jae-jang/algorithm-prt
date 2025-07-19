data = input()

lst = []
temp_digit = ''
idx = -1 # - 연산자가 처음 나오는 위치 (빼기 연산자가 처음 등장하면 그 뒤로는 모두 음수 처리)
width = 0 #연산자가 몇번 나왔는지 세기
for str in data:
    #숫자인 경우
    if str.isdigit():
        temp_digit += str
    #연산자인 경우
    else:
        lst.append(int(temp_digit))
        temp_digit = ''
        width += 1
        if idx == - 1 and str == '-':
            idx = width

lst.append(int(temp_digit))

if idx != -1:
    result = sum(lst[:idx]) - sum(lst[idx:])
else:
    result = sum(lst)

# print(idx, lst)
print(result)