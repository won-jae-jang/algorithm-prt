n = int(input())
seq = []
sort_seq = []
for i in range(n):
    number = int(input())
    seq.append(number)
    sort_seq.append(number)

sort_seq.sort()
result = []
stack = []
t_idx = 0
s_idx = 0
can_make = True #수열을 만들 수 있는가
while True:
    if t_idx == n:
        break

    target = seq[t_idx]
    #push
    if not stack or target > stack[-1]:
        stack.append(sort_seq[s_idx])
        result.append('+')
        s_idx += 1
    #pop
    elif target == stack[-1]:
        stack.pop()
        result.append('-')
        t_idx += 1
    #수열을 만들 수 없는 경우
    else:
        can_make = False
        break

if can_make:
    for x in result:
        print(x)
else:
    print('NO')






