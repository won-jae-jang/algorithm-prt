from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
words.sort()
temp = [word for word in words if len(word) == 5]
print(words)
a = bisect_left(temp, "aaaao")
b = bisect_right(temp, "zzzzo")
print(a)
print(b)
# print('---')
# print('frozen' > 'frozz')

# a = '??aaa'
# b = a.replace('?', 'z')
# print(b)