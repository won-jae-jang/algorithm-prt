from collections import Counter

ex_list1 = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi']
ex_list2 = ['kim', 'kim', 'park', 'choi', 'kim', 'kim', 'kim', 'choi', 'park', 'choi', 'dark']
ex_counter1 = Counter(ex_list1)
ex_counter2 = Counter(ex_list2)
print(list(ex_counter2 - ex_counter1)[0])
print(len(ex_counter1))
print(ex_counter1)