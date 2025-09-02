arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lst = []
lst.append([row[0] for row in arr])
print(lst)