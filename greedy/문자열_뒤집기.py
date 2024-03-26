s = input()

# 001100 -> 010 -> 1 한번만 뒤집기

zero_count = 0
one_count = 0
pre_ele = -1

for ele in s:

  if ele == '0' and pre_ele != '0':
    zero_count += 1
  elif ele == '1' and pre_ele != '1':
    one_count += 1

  pre_ele = ele

print(min(zero_count, one_count))
