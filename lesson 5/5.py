from random import randint
file = open('4.txt', 'w+')
file.seek(0)
for i in range(1, 11):
    file.write(f'{randint(1, 100)} ')
print(sum(map(int, file.readline().split())))
file.close()