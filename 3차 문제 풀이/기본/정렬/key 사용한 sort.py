array = [('banana', 2), ('apple', 5), ('carrot', 3)]

def setting(data):
    return data[1]

array.sort(key = setting)
#[('banana', 2), ('carrot', 3), ('apple', 5)]
print(array)