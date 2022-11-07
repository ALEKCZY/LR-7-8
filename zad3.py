text = input()

print("Первый символ:", text[0])
print("Последний символ:", text[-1])

if len(text) % 2 == 0:
    print("Среднего символа не существует.")
else:
    leng = int(len(text))
    sr = leng // 2
    print ("Средний символ:", text[sr])