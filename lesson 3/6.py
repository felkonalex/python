def int_func(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if set(word) <= set(letters):  # .issubset (дочернее для letters)
        return word.title()
    else:
        return
stroka = input('Введите слова через пробел - ').split()
for i in stroka:
    print(int_func(i), end=' ')