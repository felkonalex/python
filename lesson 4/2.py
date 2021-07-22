from random import randint
list = []
newlist = []
for i in range(1, 11):
    list.append(randint(0, 100))
for x in range(1, len(list)):
    if list[x] > list [x - 1]:
        newlist.append(list[x])
print(f'Исходный список - {list}')
print(f'Измененный список - {newlist}')