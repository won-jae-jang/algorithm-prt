n = int(input())

result = 0
for hour in range(n + 1):
    if '3' in str(hour):
        result += 60 * 60
    else:
        for minute in range(60):
            if '3' in str(minute):
                result += 60
                continue
            else:
                for second in range(60):
                    if '3' in str(second):
                        result += 1

print(result)