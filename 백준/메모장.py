from itertools import permutations

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for case in list(permutations(move, 4)):
    print(case)
    print(case[0][0])