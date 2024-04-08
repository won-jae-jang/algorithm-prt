h = int(input())
count = 0

for hour in range(h + 1):

  for minite in range(60):

    for second in range(60):

      if '3' in str(hour) + str(minite) + str(second):
        count += 1

print(count)