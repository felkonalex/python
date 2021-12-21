spisok = input('Введите несколько слов через пробел: ').split()
n = 1
for i in spisok:
    while len(i) > 10:
        a = list(i)
        a.pop(10)
        i = ''.join(a)
    print(f"{n}.", i)
    n += 1
