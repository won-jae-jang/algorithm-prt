from collections import deque

def preprocess_str(str_arr):
    # ex) str_arr = '[1,2,3,4]' -> [1, 2, 3, 4]
    str_arr = str_arr[1:-1]
    if str_arr:
        return deque(list(map(int, str_arr.split(','))))
    else:
        return deque([])

tc = int(input())
for _ in range(tc):
    func = input()
    n = int(input())
    arr = preprocess_str(input()) #[1,2,3,4]
    is_reverse = False
    error = False
    for f in func:
        if error:
            break
        if f == 'R':
            is_reverse = not is_reverse
        else:
            if arr:
                if is_reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True

    if error:
        print('error')
    else:
        if is_reverse:
            arr.reverse()
        lst = list(map(str, list(arr)))
        answer = '[' + ','.join(lst) + ']'
        print(answer)