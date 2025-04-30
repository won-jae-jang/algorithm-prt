from collections import deque

def preprocess_arr(str_arr):
    str_arr = str_arr.strip()[1:-1]
    if not str_arr:
        return deque()
    return deque(map(int, str_arr.split(',')))

def print_format(arr, is_reversed):
    if is_reversed:
        arr.reverse()
    print('[' + ','.join(map(str, arr)) + ']')

tc = int(input())
for t in range(tc):
    func = input().strip()
    # print('func:', func)
    n = int(input())
    str_arr = input()

    arr = preprocess_arr(str_arr) #문자 배열을 숫자 배열로 전환
    is_reversed = False
    error = False
    for c in func:
        if c == 'R':
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True
        # 첫번째 값 제거
        else:
            # print('{}번째 arr: size {}'.format(t, arr_size))
            if not arr:
                error = True
                break
            else:
                if is_reversed:
                    arr.pop()
                else:
                    arr.popleft()

    if error:
        print('error')
    else:
        print_format(arr, is_reversed)