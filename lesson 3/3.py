def summa2(*args):
    return args
a = int(input('Введите число 1 - '))
b = int(input('Введите число 2 - '))
c = int(input('Введите число 3 - '))
vals = list(summa2(a, b, c))
vals.sort(reverse=True)
print('Сумма 2-х наибольших элементов равна - ', vals[0] + vals[1])
