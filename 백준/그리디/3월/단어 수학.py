n = int(input())
score = [] # (점수, 알파벳)

#특정 알파벳이 몇번째 자리 수인지에 따라 계산해주는 함수
def cal(score, alphabet, number):
    for i in range(len(score)):
        if score[i][1] == alphabet:
            score[i][0] += 10 ** (number - 1)
            return
    score.append([10 ** (number - 1), alphabet])

for i in range(n):
    word = input()
    for j in range(len(word)):
        cal(score, word[j], len(word) - j)

score.sort(reverse=True)
result = 0
number = 9
for x, alphabet in score:
    result += x * number
    number -= 1

print(result)