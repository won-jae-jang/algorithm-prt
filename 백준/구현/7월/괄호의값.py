str = input()

def is_right(str):
    type1_left = 0 # (
    type2_left = 0 # [
    for s in str:
        if s == '(':
            type1_left += 1
        elif s == '[':
            type2_left += 1
        elif s == ')':
            if type2_left >= 1 and type1_left == 0:
                return False
            type1_left -= 1
        elif s == ']':
            if type1_left >= 1 and type2_left == 0:
                return False
            type2_left -= 1
    return True

print(is_right(str))