s = input()
if len(s) > 6:
    print('Первые 3: ', s[:3], 'Последние 3: ', s[len(s) - 3:])
else:
    print(s[0] * len(s))
