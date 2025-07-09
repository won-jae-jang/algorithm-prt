n = int(input())
words = list(input() for _ in range(n))
data = [0] * 27 #모든 알파벳의 수는 26개
# 알파벳 -> 숫자 변환 + 자리수 별 카운팅
for word in words:
    for i, alphabet in enumerate(word):
        # A -> 첫번째 인덱스
        data[int(ord(alphabet)) - int(ord('A')) + 1] += 10 ** (len(word) - i - 1)

# print(data)
# 높은 자리수 알파벳 파악
result = 0
mul_n = 9
while True:
    max_value = max(data)
    if max_value == 0:
        print(result)
        break
    max_idx = data.index(max_value) #최대 지점 인덱스
    result += max_value * mul_n
    mul_n -= 1 #9 -> 8 -> 7..
    data[max_idx] = 0 #다음 최댓값을 파악하기 위해 0으로 초기화
