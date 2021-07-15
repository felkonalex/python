list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
newlist = [i for i in range(0, len(list)) if list.count(i) == 1]
print(f'Начальный список - {list}')
print(f'Список без повторения элементов - {newlist}')