n = int(input('Введите целое положительное число - '))
a = 0
if n <= 0:
    print('Неверное число!')
else:
    while n >= 1:
        b = n % 10
        if b > a:
            a = b
        n = (n - b) / 10
    print('Наибольшая цифра в числе - ', int(a))
