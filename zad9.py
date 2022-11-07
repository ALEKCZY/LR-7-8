s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
 
a = abs(len(s1) - len(s2))
 
if len(s1) > len(s2):
    print('Вывод:', s1 * a)
else:
    print('Вывод:', s2 * a)
