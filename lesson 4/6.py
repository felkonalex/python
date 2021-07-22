# первая часть
from itertools import count
for i in count(int(input('Введите стартовое число (для остановки нажмите z) - ')), 1):
    print(i, end='')
    a = input('')
    if a == 'z':
        break

# вторая часть
list = input('Введите элементы списка через пробел: ').split()
newlist = iter(list)
for i in range(0, len(list)): # условие, при котором прекратится перебор элементов спика - последний элемент списка
    a = input()
    print(next(newlist), end='')


