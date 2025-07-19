a, b = map(int, input().split())

def add_one(a, b):
    a = int(str(a) + '1')
    while a < b:
         #2를 곱한 값이 b에 포함되는 수인 경우
         if str(a) in str(b):
             return True
         a *= 2
         
    #81이 162가 되는 경우
    if a == b:
        return True
    return False

width = 1
while a < b:
    #1을 추가하는 연산을 할 수 있다면
    if add_one(a, b):
        a = int(str(a) + '1')
    else:
        a *= 2
    width += 1

if a == b:
    print(width)
else:
    print(-1)
