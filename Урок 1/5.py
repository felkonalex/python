v = int(input('Введите сумму выручки фирмы - '))
i = int(input('Введите сумму издержек фирмы - '))
if v > i:
    print('Фирма работает в прибыль!')
    print('Рентабельность выручки составляет ', float((v-i)/v)*100, '%')
    count = int(input('Введите количество сотрудников фирмы - '))
    print('Прибыль на каждого сотрудника составляет - ', (v-i)/count)
if v == i:
    print('Извините, в задании не сказали что с этим делать :)')
if v < i:
    print('Фирма работает в убыток!')
