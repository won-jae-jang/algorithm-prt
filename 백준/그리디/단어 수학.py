n = int(input())
data = []
words = []

#모든 단어의 특정 알파벳에 대해서 숫자로 바꿔주는 함수
def change(words, alpha, num):
    for i in range(n):
        words[i] = words[i].replace(alpha, num)

def get_score(words):
    total = 0
    for word in words:
        total += int(word)
    return total

for i in range(n):
    word = input()
    words.append(word)
    for j in range(len(word)):
        data.append((len(word) - j, word[j])) #자리수,  알파벳

data.sort(reverse=True) #높은 자리수의 알파벳이 앞에 놓이게끔 정렬
process = [] #처리한 알파벳
max_num = 9
for number, alphabet in data:
    #처리되지 않은 알파벳 이라면
    if alphabet not in process:
        process.append(alphabet)
        change(words, alphabet, str(max_num))
        max_num -= 1

print(get_score(words))