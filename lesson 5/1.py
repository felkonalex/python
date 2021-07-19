with open('1.txt', 'w') as file:
    while True:
        string = input('Введите новую строку - ')
        if string == '':
            break
        file.write(f'{string} \n')
