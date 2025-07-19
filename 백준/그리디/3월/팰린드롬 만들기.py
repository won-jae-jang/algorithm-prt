name = input()
name = list(name)
name.sort()
data = [] #(알파벳, 알파벳 개수)

def is_available(name, data):
    #문자가 짝수개인 경우
    if len(name) % 2 == 0:
        for i in range(len(data)):
            #짝수로만 구성되어야 함
            if data[i][1] % 2 != 0:
                return False
        return True
    #문자가 홀수개인 경우
    else:
        count = 0 #홀수의 알파벳 개수를 세기
        for i in range(len(data)):
            if data[i][1] % 2 != 0:
                count += 1
        #홀수의 개수가 1개일때 팰린드롬을 만들 수 있음
        if count != 1:
            return False
        return True
    
prv = name[0]
width = 1
for i in range(1, len(name)):
    if name[i] == prv:
        width += 1
    else:
        data.append((prv, width))
        width = 1
        prv = name[i]

length = len(name) #이름의 길이
data.append((prv, width))
result = ['z'] * length
if is_available(name, data):
    idx = 0
    for alphabet, width in data:
        is_odd = True if width % 2 != 0 else False #홀수인가
        #홀수인 경우 가운데 위치
        if is_odd:
            result[length // 2] = alphabet
            width -= 1
        while width != 0:
            result[idx] = alphabet
            result[length - 1 - idx] = alphabet
            idx += 1
            width -= 2
    for x in result:
        print(x, end='')
else:
    print("I'm Sorry Hansoo")