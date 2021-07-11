def my_func(x, y):
    i = 2
    const = x
    if i <= -y:
        while i <= -y:
            result = const * x
            x = result
            i += 1
    elif -y == 1:
        result = x
    result = 1 / result
    return result
x = float(input('Введите действительное положительное число X - '))
y = int(input('Введите целое отрицательное число Y - '))
if x > 0 and y < 0:
    print('x в степени y =', my_func(x, y))
else:
    print('Вы ввели неверные числа!')
