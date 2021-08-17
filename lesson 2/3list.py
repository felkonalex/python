winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
a = int(input('Введите месяц (цифрой): '))
if a > 12 or a <= 0:
    print('Такого месяца не существует!')
elif a in winter:
    print('Зима')
elif a in spring:
    print('Весна')
elif a in summer:
    print('Лето')
elif a in autumn:
    print('Осень')
