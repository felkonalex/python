def delenie():
    try:
        a = float(input('Введите делимое - '))
        b = float(input('Введите делитель - '))
        c = a / b
    except ZeroDivisionError:
        print('Деление на 0!')
        return
    return c
print(f"Частное - {delenie()}")
