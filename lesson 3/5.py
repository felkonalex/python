def chisla():
    sum = 0
    while True:
        spisok = input('Введите числа через пробел, введите z для выхода -  ').split()
        for val in spisok:
            try:
                if val == 'z':
                    return sum
                else:
                    sum += int(val)
            except ValueError:
                print ('Неверное число!')
                return sum
        print(f"Сумма чисел - {sum}")
print(chisla())
