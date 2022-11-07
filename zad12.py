line=input("Введите строку: ")
c=0
for i,s in enumerate(line):
    if s.isdigit():
        c += len(s)
if c == 0:
    print("числа не обнаружены")
else:
    print("Кол-во чисел: ",c)
