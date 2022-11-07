s = input('Введите строку: ')
 
def a(s):
    if s[:3] == 'abc':
        s = 'www' + s[3:]
    else:
        s += 'zzz'
    return s
print(a(s))