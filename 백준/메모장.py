from collections import Counter

ex_list = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi']
ex_counter = Counter(ex_list)
# print(ex_counter) #Counter({'kim': 5, 'choi': 3, 'park': 2})
result = dict(ex_counter)
for i in result:
    print(i, result[i])