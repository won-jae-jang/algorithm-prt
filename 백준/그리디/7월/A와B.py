# https://growth-coder.tistory.com/231
s = input()
t = input()

while len(t) > len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

print(1 if s == t else 0)   